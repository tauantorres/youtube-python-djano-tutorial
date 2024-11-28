
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .forms import UserRegisterForm


# Create your views here.
def register(request: HttpRequest) -> HttpResponse:
    
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request=request, message=f'Your account has been created! You are now able to log in.')
            return redirect(to='login')

    else:
        form = UserRegisterForm()

    return render(
        request=request,
        template_name='users/register.html',
        context={'form': form},
    )


@login_required
def profile(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name='users/profile.html')
