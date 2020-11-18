from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = (
            'email',
            'role'
        )

class AuthUserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'password'
        )

    def create(self, validated_data):
        auth_user = User.objects.create_user(**validated_data)
        return auth_user


class AuthUserLoginCredential(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length = 128 , write_only = True)
    access =   serializers.CharField(read_only = True)  
    refresh = serializers.CharField(read_only = True)
    role = serializers.CharField(read_only = True)

    def create(self, validate_date):
        pass

    def update(self, instance , validate_date):
        pass

    def validate(self, data):
        email = data['email']
        password = data['password']
        user = authenticate(email = email , password = password)

        if user is None:
            raise serializers.ValidationError("Invalid Login Credentials")

        try:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            update_last_login(None,user)

            validation = {
                'access':access_token,
                'refresh': refresh_token,
                'email': user.email,
                'role': user.role
            }

            return validation

        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid Login Credentials")
                