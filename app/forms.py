from django import forms
from .models import Post

class Login(forms.Form):
    name = forms.CharField(
        label = 'Nome:',
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs= {
                'class': 'input'
            }
        )
    )
    password = forms.CharField(
        label = 'Senha:',
        required = True,
        max_length = 70,
        widget = forms.PasswordInput(
            attrs= {
                'class': 'input'
            }
        )
    )

class RegisterForm(forms.Form):
    name = forms.CharField(
        label = 'Nome:',
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                'class': 'input'
            }
        )
    )
    email = forms.EmailField(
        label = 'Email:',
        required = True,
        max_length = 100,
        widget = forms.EmailInput(
            attrs = {
                'class': 'input'
            }
        )
    )
    password1 = forms.CharField(
        label = 'Senha:',
        required = True, 
        max_length = 70,
        widget = forms.PasswordInput(
            attrs = {
                'class': 'input'
            }
        )
    )
    password2 = forms.CharField(
        label = 'Confirme a sua senha:',
        required = True,
        max_length = 70,
        widget = forms.PasswordInput(
            attrs = {
                'class': 'input'
            }
        )
    )

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'title']
        widgets = {
            'title': forms.TextInput(attrs = {
                'class': 'input',
                'placeholder': 'Digite o Título'
                }
            ),
            'content': forms.Textarea(
                attrs = {
                   'class': 'input',
                   'placeholder': 'Digite algo aqui',
                   'rows': 3
                }
            )
        }