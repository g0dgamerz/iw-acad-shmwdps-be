from rest_framework.authtoken.views import obtain_auth_token 
from django.urls import path
from .views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(), name = "login")
]
