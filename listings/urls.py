from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='listings'),  # root path for home page
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
]
