from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm, ProfilePictureForm
from checkout.models import Order
from products.models import Product
from django.contrib.auth import logout


@login_required
def profile(request):
    """
    Display the user's profile and handle profile updates.
    This view renders the user's profile page,
    allows the user to update their profile information,
    and displays the user's order history and wishlist.
    """
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


@login_required
def order_history(request, order_number):
    """
    Display order details for a past order.
    This view renders the order details page for a specific order.
    """
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


@login_required
def wishlist(request):
    """
    Display the user's wishlist.
    This view renders the user's wishlist page.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    wishlist = profile.wishlist.all()

    template = 'profiles/wishlist.html'
    context = {
        'wishlist': wishlist,
        'profile': profile,
    }

    return render(request, template, context)


@login_required
def upload_profile_picture(request):
    """
    Handle the upload of a user's profile picture.
    This view allows the user to upload a profile picture
    and renders the profile page after the upload.
    """
    if request.method == 'POST':
        form = ProfilePictureForm(
            request.POST,
            request.FILES,
            instance=request.user.userprofile
        )
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Profile picture uploaded successfully'
            )
            return redirect('profile')
    else:
        form = ProfilePictureForm(instance=request.user.userprofile)

    context = {
        'form': form
    }
    return render(request, 'profile.html', context)


@login_required
def delete_account(request):
    """
    Handle the deletion of a user account.
    This view allows the user to delete their account
    and redirects to the home page after deletion.
    """
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.userprofile.delete()
        user.delete()
        messages.success(
            request,
            'Your account has been deleted. We are sorry to see you go.'
        )
        return redirect('home')
    else:
        return HttpResponseBadRequest('Invalid request')
