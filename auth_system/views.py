from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate



def register(request):
    if request.method == "POST":
        pass
    else:
        form = UserCreationForm()


    return render(
        request,
        template_name="register.html"
    )




# Create your views here.

