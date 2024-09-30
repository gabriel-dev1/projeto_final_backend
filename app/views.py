from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from app.forms import Login, RegisterForm, PostForm
from .models import Post

# Create your views here.
def index(request):
    form = Login()

    if request.method == 'POST':
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
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            if form['password1'].value() != form['password2'].value():
                messages.error(request, 'senhas não são iguais.')
                return redirect('register')
            
            nome = form['name'].value()
            email = form['email'].value()
            password = form['password1'].value()

            if User.objects.filter(username=nome).exists():
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
        
    return render(request, 'register.html', {'form': form})

def home(request):
    #if not request.user.is_authenticated:
        #messages.error(request, 'Usuário não logado.')
        #return redirect('index')

    form  = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST or None)

        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.save()
            return redirect('home')
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts ,'form': form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'logout efetuado com sucesso.')
    return redirect('index')

def editar_post(request, post_id):
    post = Post.objects.get(id=post_id)
    form2 = PostForm(instance=post)
    
    if request.method == 'POST':
        form2 = PostForm(request.POST, instance=post)

        if form2.is_valid():
            form2.save()
            messages.success(request, 'post editado')
            return redirect('home')
        
    return render(request,'home.html', {'form': form2, 'post_id': post_id}) 



def deletar_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    messages.success(request, 'post deletado')
    return redirect('home')