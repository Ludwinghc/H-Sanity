from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
urlpatterns = [
    path('', views.inicioAuditor, name='inicioAuditor'),
    path('auditor/create', views.createAuditor, name='createAuditor'),
    path('auditor/view', views.viewAuditor, name='viewAuditor'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)