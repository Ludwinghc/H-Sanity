from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
urlpatterns = [
    path('', views.inicioAuditor, name='inicioAuditor'),
    path('auditor/view', views.viewAuditor, name='viewAuditor'),
    path('auditor/create', views.createAuditor, name='createAuditor'),
    path('auditor/edit', views.edit, name='editAuditor'),
    path('auditor/edit/<int:id>', views.edit, name='editAuditor'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)