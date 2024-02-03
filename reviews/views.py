from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
from products.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def product_reviews(request, product_id):
    product = Product.objects.get(pk=product_id)
    reviews = product.reviews.all()

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

    return render(request, 'reviews/product_reviews.html', {'product': product, 'reviews': reviews, 'form': form})
