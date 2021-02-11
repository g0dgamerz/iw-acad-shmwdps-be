from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    token = serializers.CharField(required=False)


    def validate(self, data):
        # super().validate(data)
        email = data['email']
        password = data['password']

        user = authenticate(email=email, password=password)
        if not user:
            raise serializers.ValidationError("Invalid Username/Password")
        data['token'], _ = Token.objects.get_or_create(user=user)
        return data

