from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Establishment
from .forms import HotelForm
from django.contrib.auth.decorators import login_required
from account.decorators import allowedUsers

# Create your views here.

@login_required(login_url='login')
@allowedUsers(allowedRoles='auditor')
def view(request):
    hoteles = Establishment.objects.all()
    return render(request, 'hotel/viewHotel.html', {'hoteles' : hoteles})

@login_required(login_url='login')
@allowedUsers(allowedRoles='auditor')
def create(request):
    form = HotelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('hotelView')
    return render(request, 'hotel/createHotel.html', {'form' : form})

@login_required(login_url='login')
@allowedUsers(allowedRoles='auditor')
def edit(request, id):
    hotel = Establishment.objects.get(id=id)
    form = HotelForm(request.POST or None, request.FILES or None, instance=hotel)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('hotelView')
    return render(request, 'hotel/editHotel.html', {'form' : form})