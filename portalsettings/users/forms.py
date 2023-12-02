from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm

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
    
    profession = (
        (1, 'Студент'),
        (2, 'Фронтенд-разработчик'),
        (3, 'Бэкенд-разработчик'),
        (4, 'Фуллстек-разработчик'),
        (5, 'Разработчик игр'),
        (6, 'Мобильный разработчик'),
        (7, 'DevOps-инженер'),
        (8, 'Системный администратор'),
        (9, 'Тестировщик'),
        (10, 'Дата-аналитик'),
        (11, 'Дата-сайентист')
    )

    lvl = (
        (1, 'Студент'),
        (2, 'Стажёр'),
        (3, 'Junior'),
        (4, 'Middle'),
        (5, 'Senior')
    )

    type_of_profession = forms.ChoiceField(choices=profession, required=True, label='Какая у вас профессия?', widget= forms.Select)



    skill_level = forms.ChoiceField(choices=lvl, required=True, label='Насколько вы оцениваете ваши навыки?', widget= forms.RadioSelect)

    class Meta:
        model = User
        fields = ['email', 'username', 'type_of_profession', 'skill_level', 'password1', 'password2']

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