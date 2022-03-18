from django.shortcuts import redirect, render
from django.http import HttpResponse
from Login import models

from Login.forms import RegistrationForm

# Create your views here.
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
