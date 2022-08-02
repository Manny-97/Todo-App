from django.urls import path
from .views import activate_user, register, login_user, logout_user
urlpatterns = [
    path('login', login_user, name='login'),
    path('register', register, name='register'),
    path('logout_user', logout_user, name='logout_user'),
    path('activate_user', activate_user, name='activate')
]