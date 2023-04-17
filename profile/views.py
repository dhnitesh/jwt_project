from django.shortcuts import render

# Create your views here.

# api view
from rest_framework import generics
from .models import UserProfile
from .serializers import UserProfileSerializer

# get self profile from jwt token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UserProfileSerializer(request.user.profile)
        return Response(serializer.data)
    
    def put(self, request):
        serializer = UserProfileSerializer(request.user.profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


# Create your views here.

# api view
from rest_framework import generics
from .models import UserProfile
