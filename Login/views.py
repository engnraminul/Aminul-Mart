from django.shortcuts import redirect, render
from django.http import HttpResponse
from Login import models

from Login.forms import RegistrationForm, ProfileForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

from Order.models import Cart, CartToOrder
from Payment.models import BillingAddress
from Login.models import Profile
from django.views.generic import TemplateView
from Payment.forms import BillingAddressForm
#registation function
def register(request):
    if request.user.is_authenticated:
        return HttpResponse('You are authenticated!')
    else:
        form = RegistrationForm()
        if request.method == 'post' or request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse('Your Account has been created!')

    context = {
        'form': form
    }
    return render(request, 'login/register.html', context)


def user_login(request):
    if request.user.is_authenticated:
        return HttpResponse('You are allready logged!')
    else:
        if request.method == 'POST' or request.method == 'post':
            user_email = request.POST.get('user_email')
            password = request.POST.get('password')
            login_user = authenticate(request, email=user_email, password=password)
            if login_user is not None:
                login(request, login_user)
                return HttpResponse('You are login successfully!')
            else:
                return HttpResponse('User name or password incorrect!')
    return render(request, 'login/login.html')



class ProfileView(TemplateView):
    def get(self, request, *args, **kwargs):
        orders = CartToOrder.objects.filter(user = request.user, ordered=True)
        billingaddress = BillingAddress.objects.get(user=request.user)
        billingaddressform = BillingAddressForm(instance=billingaddress)

        profile_obj = Profile.objects.get(user=request.user)
        profile_form = ProfileForm(instance=profile_obj)

        context = {
            'orders': orders,
            'billingaddress': billingaddressform,
            'profile_form': profile_form,
        }
        return render(request, 'login/profile.html', context)


    def post(self, request, *args, **kwargs):
        if request.method == 'POST' or request.method =='pot':
            billingaddress = BillingAddress.objects.get(user=request.user)
            billingaddressform = BillingAddressForm(request.POST, instance=billingaddress)

            profile_obj = Profile.objects.get(user=request.user)
            profile_form = ProfileForm(request.POST, instance=profile_obj)

            if billingaddressform.is_valid() or ProfileForm.is_valid():
                billingaddressform.save()
                profile_form.save()
                return redirect('Login:profile')
