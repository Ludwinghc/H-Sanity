from django.urls import path
from . import views

urlpatterns = [
    path('hotel/audit/<int:id>/', views.audits, name='auditView'),
    path('hotel/audit/create/<int:id>/', views.createAudit, name='createAudit'),
]