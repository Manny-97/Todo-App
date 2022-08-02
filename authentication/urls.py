from django.urls import path
from .views import register, login_user
urlpatterns = [
    path('login', login_user, name='login'),
    path('register', register, name='register'),
]