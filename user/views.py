from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import Device
from .serializers import LogOutSerializer, UserSerializer, LoginSerializer

User = get_user_model()

class SignUpView(CreateAPIView):
    authentication_classes = []
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SignInView(APIView):
    authentication_classes = []
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            device_id = request.data.get('device_id')
            if device_id is None:
                return Response({'message': 'device_id field is required'}, status=400)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                Device.get_or_create_device(user=user, device_id=device_id)
                return Response(UserSerializer(user).data)
            else:
                return Response({'message': 'Invalid credentials.'}, status=401)

        return Response(serializer.errors, status=400)
    
    
class SignOutView(APIView):
    authentication_classes = []
    def post(self, request):
        serializer = LogOutSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        device = Device.get_active_device(serializer.validated_data['device_id'])
        device.is_active = False
        device.save()
        return Response({'message': 'Success'}, status=200)
    
    
class MeView(APIView):
    authentication_classes = []
    
    def post(self, request):
        serializer = LogOutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        device = Device.get_active_device(serializer.validated_data['device_id'])
        return Response(UserSerializer(device.user).data)
    
    
class UserDeleteView(APIView):
    authentication_classes = []
    
    def post(self, request):
        serializer = LogOutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        device = Device.get_active_device(serializer.validated_data['device_id'])
        device.is_active = False
        device.save()
        user = device.user
        user.is_active = False
        user.save()
        return Response(UserSerializer(device.user).data)

        
