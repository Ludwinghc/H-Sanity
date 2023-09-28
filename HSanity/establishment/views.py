from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Establishment
from .forms import EstablishmentForm

# Create your views here.

def view(request):
    hoteles = Establishment.objects.all()
    return render(request, 'hotel/viewHotel.html', {'hoteles' : hoteles})

def create(request):
    form = EstablishmentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('hotelView')
    return render(request, 'hotel/createHotel.html', {'form' : form})

def edit(request, id):
    hotel = Establishment.objects.get(id=id)
    form = EstablishmentForm(request.POST or None, request.FILES or None, instance=hotel)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('hotelView')
    return render(request, 'hotel/editHotel.html', {'form' : form})