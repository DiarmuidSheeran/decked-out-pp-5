from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
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

    products = Product.objects.all()

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
    reviews = product.reviews.all()
    average_rating = product.calculate_average_rating()
    user = request.user

    if user.is_authenticated:
        has_ordered_product = Order.objects.filter(user_profile=user.userprofile, lineitems__product=product).exists()
    else:
        has_ordered_product = False
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
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
