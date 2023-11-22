from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('hotel/audit/<int:id>/', views.audits, name='auditView'),
    path('hotel/audit/create/<int:id>/', views.createAudit, name='createAudit'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)