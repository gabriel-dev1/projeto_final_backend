from django.urls import path
from app.views import index, register, home, logout

urlpatterns = [ 
    path('', index, name='index'), 
    path('register', register, name='register'),
    path('home', home, name='home'),
    path('logout', logout, name='logout'),
]