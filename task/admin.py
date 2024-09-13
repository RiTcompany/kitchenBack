from django.contrib import admin

from .models import Task, TaskStatusChoices

# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('article', 'user', 'status', 'create_at', 'update_at')
    search_fields = ('article', 'user__username')
    list_filter = ('status', 'create_at', 'update_at')
    actions = ['change_status_in_work', 'change_status_packed', 'change_status_shipped']
    
    def change_status_in_work(self, request, queryset):
        queryset.update(status=TaskStatusChoices.IN_WORK)
        
    def change_status_packed(self, request, queryset):
        queryset.update(status=TaskStatusChoices.PACKED)
        
    def change_status_shipped(self, request, queryset):
        queryset.update(status=TaskStatusChoices.SHIPPED)
        
    change_status_in_work.short_description = 'Установить статус в работе'
    change_status_packed.short_description = 'Установить статус в упакован'
    change_status_shipped.short_description = 'Установить статус в отгружен'