from typing import Any
from django.db import models
from django.urls import reverse

# Create your models here.

class Video(models.Model):
    name = models.CharField(max_length=512, verbose_name='Название')
    link = models.CharField(max_length=512, verbose_name='Ссылка')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    sequence_number = models.IntegerField(verbose_name='Порядковый номер')
    
    def __str__(self):

        return self.name
    
    def get_absolute_url(self):
        return reversed('photo-detail', kwargs={'pk': self.pk})
    
    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
        ordering = ['sequence_number']
    
    
class Photo(models.Model):
    image = models.ImageField(upload_to='photos/', verbose_name='Изображение')
    name = models.CharField(max_length=512, verbose_name='Название')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    sequence_number = models.IntegerField(null=True, blank=True, verbose_name='Порядковый номер')
    
    def get_absolute_url(self):
        return reverse('photo-detail', kwargs={'pk': self.pk})
    
    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ['sequence_number']
        
        
class NewProduct(models.Model):
    image = models.ImageField(upload_to='photos/', verbose_name='Изображение')
    name = models.CharField(max_length=512, verbose_name='Название')
    link = models.CharField(max_length=512, verbose_name='Ссылка')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    
    def get_absolute_url(self):
        return reverse('new-product-detail', kwargs={'pk': self.pk})
    
    class Meta:
        verbose_name = 'Новинка'
        verbose_name_plural = 'Новинки'
        ordering = ['-update_at']

