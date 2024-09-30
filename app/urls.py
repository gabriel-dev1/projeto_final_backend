from django.urls import path
from app.views import index, register, home, logout, editar_post, deletar_post

urlpatterns = [ 
    path('', index, name='index'), 
    path('register', register, name='register'),
    path('home', home, name='home'),
    path('logout', logout, name='logout'),
    path('editar-post/<int:post_id>', editar_post, name='editar_post'),
    path('deletar-post/<int:post_id>', deletar_post, name='deletar_post'),
]