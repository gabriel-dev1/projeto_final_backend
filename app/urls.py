from django.urls import path
from app.views import index, register, home

urlpatterns = [ 
    path('', home, name='index'), 
    path('register', register, name='register'),
    path('home', home, name='home'),
]