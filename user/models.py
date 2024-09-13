from django.db import models
from django.contrib.auth.models import User
from rest_framework.exceptions import PermissionDenied, AuthenticationFailed

# Create your models here.
class Device(models.Model):
    device_id = models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='devices')
    update_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['device_id']),
            models.Index(fields=['device_id', 'is_active'])
        ]
        unique_together = ('user', 'device_id')
        
    @classmethod
    def get_or_create_device(cls, user, device_id):
        user_active_devices = cls.objects.filter(user=user, is_active=False)
        try:
            device = user_active_devices.get(device_id=device_id)
            device.is_active = True
            device.save()
            return device
        except cls.DoesNotExist:
            if cls.objects.filter(device_id=device_id, is_active=True).exists():
                raise PermissionDenied(detail='Device with provided ID is already used by another user') 
            return cls.objects.create(user=user, device_id=device_id,)
        
    @classmethod
    def get_active_device(cls, device_id):
        try: 
            return cls.objects.get(device_id=device_id, is_active=True)
        except cls.DoesNotExist:
            raise AuthenticationFailed(detail='Device with provided ID not found')