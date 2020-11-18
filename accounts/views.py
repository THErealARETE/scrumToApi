from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import *

from .models import User


class ListUsersView(APIView):
    serializer_class = ListUserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        if user.role != 1 :
            response = {
                'success': False,
                 'status_code': status.HTTP_403_FORBIDDEN,
                'message': 'You are not authorized to perform this action'
            }
            return Response(response, status = status_code)

        else:
            users = User.objects.all()
            serializer = self.serializer_class(users, many = True)
            status_code = status.HTTP_200_OK
            response = {
                 'success': True,
                 'status_code': status_code,
                'message': 'Successfully listed all user',
                'users': serializer.data 
            }    

            return Response(response , status = status_code)



class LoginView(APIView):
    serializer_class = AuthUserLoginCredential
    permission_classes = (AllowAny, )
    # queryset = User.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception = True)

        if valid:
            status_code = status.HTTP_200_OK

            response = {
                'statusCode': status_code,
                'message': 'User logged in successfully',
                'access': serializer.data['access'],
                'refresh': serializer.data['refresh'],
                'authenticatedUser': {
                    'email': serializer.data['email'],
                    'role': serializer.data['role']
                }
            }    

            return Response(response , status = status_code)


class AuthUserRegistrationView(APIView):
    serializer_class = AuthUserRegistrationSerializer
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED

            response = {
                'success': True,
                'statusCode': status_code,
                'message': 'User successfully registered!',
                'user': serializer.data
            }

            return Response(response, status=status_code)

