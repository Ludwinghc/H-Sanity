from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
urlpatterns = [
    path('auditor/', views.inicioAuditor, name='inicioAuditor'),
    path('auditor/view-Auditor', views.viewAuditor, name='viewAuditor'),
    path('auditor/create-Auditor', views.create, name='createAuditor'),
    path('auditor/edit-Auditor', views.edit, name='editAuditor'),
    path('auditor/edit-Auditor/<int:id>', views.edit, name='editAuditor'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)