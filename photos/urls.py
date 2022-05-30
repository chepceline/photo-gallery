from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.gallery, name='gallery'),
    # path('photo<str:pk>,<category_name>/', views.viewPhoto, name='photo'),
    path( 'search/', views.search_image, name='search_image'),
    path('location<image_location>/)', views.location_filter, name='location_filter')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
