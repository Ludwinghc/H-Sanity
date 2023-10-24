from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logOutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('', views.home, name='auditorHome'),
]