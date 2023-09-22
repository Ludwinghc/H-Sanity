from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
urlpatterns = [
    path('auditor/', views.inicioAuditor, name='inicioAuditor'),
    path('auditor/view', views.viewAuditor, name='viewAuditor'),
    path('auditor/create', views.create, name='create'),
    path('auditor/edit', views.edit, name='edit'),
    path('auditor/edit/<int:id>', views.edit, name='edit'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)