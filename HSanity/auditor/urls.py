from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
urlpatterns = [
    path('auditor/', views.inicio, name='inicioAuditor'),
    path('auditor/view', views.view, name='viewAditor'),
    path('auditor/create', views.create, name='createAuditor'),
    path('auditor/edit', views.edit, name='editAuditor'),
    path('auditor/edit/<int:id>', views.edit, name='editAuditor'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)