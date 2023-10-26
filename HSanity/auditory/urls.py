from django.urls import path
from . import views

urlpatterns = [
    path('hotel/audits', views.audits, name='auditView'),
    path('hotel/createAudit', views.createAudit, name='createAudit'),
]