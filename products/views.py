from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q, Case, When, F, DecimalField, Avg
from .models import Product, Category, ProductStatistics
from django.db.models.functions import Lower
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from profiles.models import UserProfile
from reviews.models import Review
from checkout.models import Order
from .forms import ProductForm

# Create your views here.

def all_products(request):

    products = Product.objects.annotate(
        average_rating=Avg('reviews__rating')
    )

    for product in products:
        product.average_rating = product.calculate_average_rating()
   
    query = None
    categories = None
    sort = None
    direction = None
    filter_type = None

    if 'filter_type' in request.GET:
        filter_type = request.GET['filter_type']

    if filter_type == 'new_arrivals':
        products = products.filter(new_arrival=True)
    elif filter_type == 'special_offers':
        products = products.filter(Q(is_on_promotion=True) & Q(clearance=False))
    elif filter_type == 'clearance':
        products = products.filter(clearance=True)
    elif filter_type == 'all_offers':
        products = products.filter(Q(is_on_promotion=True) | Q(clearance=True) | Q(new_arrival=True))

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
            if sortkey == 'price':
                if direction == 'asc':
                    products = products.annotate(
                        sorted_price=Case(
                            When(is_on_promotion=True, then='promotion_price'),
                            default='price',
                            output_field=DecimalField()
                        )
                    ).order_by(F('sorted_price').asc(nulls_last=True))
                elif direction == 'desc':
                    products = products.annotate(
                        sorted_price=Case(
                            When(is_on_promotion=True, then='promotion_price'),
                            default='price',
                            output_field=DecimalField()
                        )
                    ).order_by(F('sorted_price').desc(nulls_last=True))
            elif sortkey == 'rating':
                if direction == 'asc':
                    products = products.order_by('average_rating')
                elif direction == 'desc':
                    products = products.order_by('-average_rating')
            else:
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
                products = products.order_by(sortkey)
        
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
    
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'filter_type': filter_type,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):

    product = get_object_or_404(Product, pk=product_id)
    reviews = product.reviews.filter(reviewer_name=request.user)
    average_rating = product.calculate_average_rating()
    user = request.user
    has_ordered_product = False

    if user.is_authenticated:
        has_ordered_product = Order.objects.filter(user_profile=user.userprofile, lineitems__product=product).exists()
        

    context = {
        'product': product,
        'reviews': reviews,
        'average_rating': average_rating,
        'has_ordered_product': has_ordered_product,
    }

    return render(request, 'products/product_detail.html', context)

@login_required
def wishlist(request, sku, *args, **kwargs):
    product_wish = get_object_or_404(Product, sku=sku)
    user = request.user
    user_profile = user.userprofile

    liked = False

    if product_wish.wishlist.filter(id=request.user.id).exists():
        product_wish.wishlist.remove(request.user)
        user_profile.wishlist.remove(product_wish)
        liked = False
    else:
        product_wish.wishlist.add(request.user)
        user_profile.wishlist.add(product_wish)
        liked = True

    return JsonResponse({'wishlist_count': product_wish.wishlist.count(), 'liked': liked})

def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def product_statistics(request):
    sold_products = Product.objects.filter(productstatistics__total_sold__gt=0)
    recommend_promo_products = Product.objects.filter(productstatistics__total_sold__lte=5, is_on_promotion=False)

    sort_by = request.GET.get('sort_by')
    sort_by = request.GET.get('sort_by')
    if sort_by == 'sales_asc':
        sold_products = sold_products.order_by('productstatistics__total_sold')
    elif sort_by == 'sales_desc':
        sold_products = sold_products.order_by('-productstatistics__total_sold')
    elif sort_by == 'purchased_asc':
        sold_products = sold_products.order_by('productstatistics__times_purchased')
    elif sort_by == 'purchased_desc':
        sold_products = sold_products.order_by('-productstatistics__times_purchased')
    
    context = {
        'sold_products': sold_products,
        'recommend_promo_products': recommend_promo_products,
        }

    return render(request, 'products/product_statistics.html', context )

    
