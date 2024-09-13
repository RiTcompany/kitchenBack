from django.urls import path
from .views import *

urlpatterns = [
    path('videos/', VideoListView.as_view(), name='video-list'),
    path('videos/<int:pk>/', VideoDetailView.as_view(), name='video-detail'),
    path('photos/', PhotoListCreateView.as_view(), name='photo-list'),
    path('photos/<int:pk>/', PhotoDetailView.as_view(), name='photo-detail'),
    path('new-products/', NewProductListCreateView.as_view(), name='new-product-list'),
    path('new-products/<int:pk>/', NewProductDetailView.as_view(), name='new-product-detail'),
]
