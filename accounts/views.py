from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from accounts.forms import UserCreationForm, LoginForm

# Create your views here.


def login_view(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'accounts/login.html', {"form": form})
    else:
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                email = form.cleaned_data.get("email"),
                password = form.cleaned_data.get("password"),
            )
            if user:
                login(request, user)
                return redirect('post-list')
            return render(request, "accounts/login.html", {"form": form, "message": "user not found"})
        return render(request, "accounts/login.html", {"form": form})
                

def register_view(request):
    if request.method == "GET":
        form = UserCreationForm()
        return render(request ,"accounts/register.html", {"form": form})
    else:
        form = UserCreationForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, "accounts/register.html", {"form": form})