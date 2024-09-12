from django.shortcuts import render, redirect
from app.forms import Login, RegisterForm, PostForm
from .models import Post
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.
def index(request):
    form = Login()

    if request.method == 'post':
        form = Login(request.POST)

        if form.is_valid():
            name = form['name'].value()
            password = form['password'].value()

        user = auth.authenticate(
            request,
            username = name,
            password = password,
         )

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'logado com sucesso.')
            return redirect('home')
        else:
            messages.error(request, 'erro ao afetuar login.')
            return redirect('index')
        
    return render(request, 'index.html', {'form': form})

def register(request):
    register = RegisterForm()

    if request.method == 'post':
        form = RegisterForm(request.POST)

        if form.is_valid():

            if form['password1'].value() != form['password2']:
                messages.error(request, 'senhas não são iguais.')
                return redirect('register')
            
            nome = form['name'].value()
            email = form['email'].value()
            password = form['password1'].value()

            if User.objects.filter(username = nome).exists():
                messages.error(request, 'esse usuário já existe')
                return redirect('register')
            
            user = User.objects.create_user(
              username = nome,
              email = email ,
              password = password,
            )
            user.save()
            messages.success(request, 'cadastro efetuado')
            return redirect('index')
        
    return render(request, 'register.html', {'form': register})

def home(request):
    form  = PostForm()
    if request.method == 'post':
        form = PostForm(request.POST or None)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
        posts = Post.objects.all().order_by('-created_at')
        
    return render(request, 'home.html' , {'posts': posts} , {'form': form})