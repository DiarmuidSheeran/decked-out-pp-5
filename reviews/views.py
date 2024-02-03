from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
from products.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from checkout.models import Order

@login_required
def product_reviews(request, product_id):

    product = Product.objects.get(pk=product_id)
    existing_review = Review.objects.filter(product=product, reviewer_name=request.user).first()
    user = request.user
    has_ordered_product = Order.objects.filter(user_profile=user.userprofile, lineitems__product=product).exists()

    if existing_review:
        messages.error(request, f'You have already left a review on this product!')
        return redirect('product_detail', product_id=product_id)

    reviews = product.reviews.all()

    if has_ordered_product:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.product = product
                review.reviewer_name = request.user
                review.save()
                return redirect('product_detail', product_id=product_id)
        else:
            form = ReviewForm()
    else:
        messages.error(request, f'You havent purchased this product')
        return redirect('product_detail', product_id=product_id)

    return render(request, 'reviews/product_reviews.html', {'product': product, 'reviews': reviews, 'form': form})
