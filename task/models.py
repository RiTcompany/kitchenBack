from django.db import models
from django.urls import reverse

# Create your models here.

class TaskStatusChoices(models.TextChoices):
    WRITED = 'writed', 'Записан'
    IN_WORK = 'in_work', 'В работе'
    PACKED = 'packed', 'Упакован'
    SHIPPED = 'shipped', 'Отгружен'


class Task(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    article = models.TextField(verbose_name='Артикул')
    status = models.CharField(max_length=24, choices=TaskStatusChoices.choices, default=TaskStatusChoices.WRITED, verbose_name='Статус')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    
    def __str__(self):
        return f'{self.article} - {self.status}'
    
    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-update_at']
