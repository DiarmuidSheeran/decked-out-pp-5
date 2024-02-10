from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm, ProfilePictureForm
from checkout.models import Order
from products.models import Product

def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    wishlist = profile.wishlist.all()

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
    
    form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'profile': profile,
        'orders': orders,
        'wishlist': wishlist,
        'on_profile_page': True
    }

    return render(request, template, context)

def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    discount_code = None
    discount_percentage = None

    if order.discount_code:
        discount_code = order.discount_code
        discount_percentage = order.discount_code.discount_amount

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'discount_code': discount_code,
        'discount_percentage': discount_percentage,
        'from_profile': True,
    }

    return render(request, template, context)

def wishlist(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    wishlist = profile.wishlist.all()

    template = 'profiles/wishlist.html'
    context = {
        'wishlist': wishlist,
        'profile': profile,
    }

    return render(request, template, context)

def upload_profile_picture(request):
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile picture uploaded successfully')
            return redirect('profile')
    else:
        form = ProfilePictureForm(instance=request.user.userprofile)

    context =  {
        'form': form
        }
    return render(request, 'profile.html', context)
    