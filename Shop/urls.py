from django.urls import path
from .views import base, home, login, registration, logout, profile

urlpatterns = [
    path('base/', base, name='base'),
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('registration/', registration, name='registration'),
    path('profile/', profile, name='profile'),
]