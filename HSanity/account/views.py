from django.shortcuts import render, redirect, get_object_or_404
from establishment.models import Establishment
from auditory.models import SectionResult, Section
from .forms import CreateUserForm
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
    return render(request, "account/login.html", {})

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
    return render(request, "account/register.html", {"form": form})


@login_required(login_url="login")
@allowedUsers(allowedRoles='auditor, user')
def home(request):
    establishments = Establishment.objects.all()
    establishmentAudit = []

    for establishment in establishments:
        latestAudit = establishment.audit_set.last()
        if latestAudit:
            sectionResults = getSectionResultsForEstablishment(establishment)
            establishmentAudit.append((establishment, latestAudit, sectionResults))

    context = {
        "establishmentAudit": establishmentAudit,
    }

    return render(request, "account/dashboard.html", context)

def getSectionResultsForEstablishment(establishment):
    latestAudit = establishment.audit_set.last()
    if latestAudit:
        sectionResults = SectionResult.objects.filter(audit=latestAudit)
        return sectionResults
    return None