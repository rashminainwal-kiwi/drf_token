from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializer import RegisterSerializer, UserSerializer


# Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def get(self, request):
        a = User.objects.all()
        return Response({'a': a})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })
