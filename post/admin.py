from django.contrib import admin

from post.models import NewProduct, Photo, Video

# Register your models here.


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('name',  'create_at', 'update_at')
    search_fields = ('name', 'link')
    list_filter = ('create_at', 'update_at')
    
    
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_at', 'update_at')
    search_fields = ('name',)
    list_filter = ('create_at', 'update_at')
    
    
@admin.register(NewProduct)
class NewProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'create_at', 'update_at')
    search_fields = ('name', 'link')
    list_filter = ('create_at', 'update_at')
    