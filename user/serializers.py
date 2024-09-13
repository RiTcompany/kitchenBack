from django.contrib.auth import get_user_model
from rest_framework import serializers



User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
            }
        
    def create(self, validated_data):
        passwd = validated_data.pop("password") 
        user = User(**validated_data)
        user.set_password(passwd)
        user.save()
        
        return user
    
    def validate_email(self, value):
        email = value.lower()
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("This email is already in use.")
        return email
    

class LogOutSerializer(serializers.Serializer):
    device_id = serializers.CharField(write_only=True)
   

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)