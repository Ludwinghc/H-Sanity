from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'general/home.html')

def view(request):
    return render(request, 'hotel/view.html')

def create(request):
    return render(request, 'hotel/create.html')