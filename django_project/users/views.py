
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest

from django.contrib import messages
from .forms import UserRegisterForm


# Create your views here.
def register(request: HttpRequest) -> HttpResponse:
    
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request=request, message=f'Account created for {username}!')
            return redirect(to='blog-home')

    else:
        form = UserRegisterForm()

    return render(
        request=request,
        template_name='users/register.html',
        context={'form': form},
    )
