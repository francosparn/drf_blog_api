from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.api.serializers import UserRegisterSerializer, UserInfoSerializer, UserUpdateSerializer


# Register User
class UserRegisterView(APIView):
    def post(self, request):
        # Inside "request.data" is where all the user information is in the body of the HTTP request (POST)
        serializer = UserRegisterSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            # Save user
            serializer.save()
            # Send user data
            return Response(serializer.data)
        
        # If the user registration is not successfully executed, an error is returned
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    

# User Information
class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]
    
    # Get user data
    def get(self, request):
        # Inside "request.user" is where all the authenticated user information is
        serializer = UserInfoSerializer(request.user)
        return Response(serializer.data)
    
    # Update user data
    def put(self, request):
        # Get user id
        user = User.objects.get(id=request.user.id)
        # We pass the user data (user) and the updated data (request.data)
        serializer = UserUpdateSerializer(user, request.data)
        
        if serializer.is_valid(raise_exception=True):
            # Save new data
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    