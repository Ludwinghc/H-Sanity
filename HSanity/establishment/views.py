from django.shortcuts import render
from .models import Establishment
# Create your views here.

def home(request):
    return render(request, 'general/home.html')

def view(request):
    hoteles = Establishment.objects.all()
    return render(request, 'hotel/view.html', {'hoteles' : hoteles})

def create(request):
    return render(request, 'hotel/create.html')

def edit(request):
    return render(request, 'hotel/edit.html')