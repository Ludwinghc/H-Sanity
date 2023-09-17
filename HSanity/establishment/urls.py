from django.urls import path
from . import views

urlpatterns = [
    path('hotel/', views.home, name='home'),
    path('hotel/view', views.view, name='view'),
    path('hotel/create', views.create, name='create'),
]
