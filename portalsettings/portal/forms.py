from .models import News
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput
from django.contrib.auth.models import User

class NewsForm(ModelForm):

    class Meta():
        model = News
        fields = ['title', 'text', 'date', 'author']

        widgets = {
            "title": TextInput(attrs= {
                'class': 'form-control',
                'placeholder': 'Тема'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст',
                
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст'
            }),
            "author": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст',
                'disabled': 'disabled'
            })
        }