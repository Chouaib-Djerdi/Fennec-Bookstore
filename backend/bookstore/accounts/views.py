from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login
from . import models
from django import forms
from .forms import CustomUserCreationForm
from mainapp.models import Customer

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            customer = Customer.objects.create(user=user)
            login(request, user)
            return redirect(reverse('mainapp:main-page'))
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect(reverse('mainapp:main-page'))
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/register.html', {'form': form})