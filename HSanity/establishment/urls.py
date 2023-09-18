from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('hotel/', views.home, name='home'),
    path('hotel/view', views.view, name='view'),
    path('hotel/create', views.create, name='create'),
    path('hotel/edit', views.edit, name='edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
