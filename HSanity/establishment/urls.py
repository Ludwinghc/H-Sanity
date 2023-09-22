from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hotel/view', views.view, name='view'),
    path('hotel/create', views.create, name='create'),
    path('hotel/edit', views.edit, name='edit'),
]
