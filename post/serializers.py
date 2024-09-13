from rest_framework import serializers

from post.models import NewProduct, Photo, Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'name', 'link', 'create_at', 'update_at','sequence_number', 'url')
        extra_kwargs = {
            'url': {'view_name': 'video-detail', 'lookup_field': 'pk'},
        }
        

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'image', 'name', 'create_at', 'update_at','sequence_number', 'url')
        extra_kwargs = {
            'url': {'view_name': 'photo-detail', 'lookup_field': 'pk'},
        }
        
class NewProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewProduct
        fields = ('id', 'name', 'image', 'create_at', 'update_at', 'link', 'url')
        extra_kwargs = {
            'url': {'view_name': 'new-product-detail', 'lookup_field': 'pk'},
        }