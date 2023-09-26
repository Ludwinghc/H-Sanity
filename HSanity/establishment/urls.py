from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('hotel/view', views.view, name='hotelView'),
    path('hotel/create', views.create, name='createHotel'),
    path('hotel/edit', views.edit, name='editHotel'),
    path('hotel/edit/<int:id>', views.edit, name='editHotel'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
