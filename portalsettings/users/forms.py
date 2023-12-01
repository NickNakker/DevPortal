from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm, UsernameField

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField(
        required=True, 
        label='Почта',
        widget= forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите почту'})
        )
    username = forms.CharField(
        required=True, 
        label='Логин', 
        help_text='Нельзя вводить символы @',
        widget= forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
        )
    
    #some = forms.ModelChoiceField(queryset=User.objects.all())
    
    password1 = forms.CharField(
        required=True, 
        label='Пароль', 
        help_text='Пароль не должен быть простым',
        widget= forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'})
        )
    password2 = forms.CharField(
        required=True, 
        label='Подтвердите пароль',
        widget= forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Проверка пароля'})
        )
    

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите логин', 'id': ''}))
    password = forms.CharField(label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите пароль',
            'id': ''
        }
))