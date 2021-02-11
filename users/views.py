from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def login(request):
    email = request.data.get("email")
    password = request.data.get("password")
    print(email,password)
    user = authenticate(request, email=email, password=password)
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({"Token": token.key})
    else:
        return Response(status=401)



