from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from .serializers import UserLoginSerializer


class LoginView(APIView):

    def post(self, request):
        userLoginSerializer = UserLoginSerializer(data=request.data)
        if userLoginSerializer.is_valid():
            token = userLoginSerializer.validated_data['token'].key
            return Response({"token": token })
        return Response(status=401)



