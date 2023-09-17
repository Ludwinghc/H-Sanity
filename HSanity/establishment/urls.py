from django.urls import path
from . import views

urlpatterns = [
    path('hotel/', views.index, name='index'),
    
]
