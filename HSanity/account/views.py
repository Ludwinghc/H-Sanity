from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Auditor
from .forms import AuditorForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticatedUser, allowedUsers

# Create your views here.

@unauthenticatedUser
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("auditorHome")
        else:
            messages.info(request, "Username or password is incorrect")
    return render(request, "account/general/login.html", {})

def logOutUser(request):
    logout(request)
    return redirect("login")

@unauthenticatedUser
def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user =form.save()
            group = Group.objects.get(name='user')
            user.groups.add(group)
            return redirect("login")
    return render(request, "account/general/register.html", {"form": form})


@login_required(login_url="login")
@allowedUsers(allowedRoles='auditor, user')
def home(request):
    return render(request, "account/dashboard.html")

