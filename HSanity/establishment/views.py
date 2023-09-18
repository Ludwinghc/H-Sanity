from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Establishment
from .forms import EstablishmentForm

# Create your views here.

def home(request):
    return render(request, 'general/home.html')

def view(request):
    hoteles = Establishment.objects.all()
    return render(request, 'hotel/view.html', {'hoteles' : hoteles})

def create(request):
    form = EstablishmentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('view')
    return render(request, 'hotel/create.html', {'form' : form})

def edit(request):
    return render(request, 'hotel/edit.html')