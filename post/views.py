from django.shortcuts import render
from rest_framework import generics

from post.serializers import *

# Create your views here.


class VideoListView(generics.ListAPIView):
    authentication_classes = []
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    
class VideoDetailView(generics.RetrieveAPIView):
    authentication_classes = []
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    
    
class PhotoListCreateView(generics.ListAPIView):
    authentication_classes = []
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    

class PhotoDetailView(generics.RetrieveAPIView):
    authentication_classes = []
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    

class NewProductListCreateView(generics.ListAPIView):
    authentication_classes = []
    queryset = NewProduct.objects.all()
    serializer_class = NewProductSerializer
    
class NewProductDetailView(generics.RetrieveAPIView):
    authentication_classes = []
    queryset = NewProduct.objects.all()
    serializer_class = NewProductSerializer