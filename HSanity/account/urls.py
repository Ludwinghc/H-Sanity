from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='auditorHome'),
    path('auditor/', views.viewAuditor, name='viewAuditor'),
    path('auditor/create', views.createAuditor, name='createAuditor')
]