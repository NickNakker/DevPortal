from django.shortcuts import render,redirect
from .models import News #Импорт таблицы из БД
from .forms import NewsForm #Иморт отредактированной формы из бд для презентации в html
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    # news = [
    #     {
    #         'title': 'Наша первая статья',
    #         'text': 'Полный текст статьи',
    #         'date': '13.08.1990',
    #         'author': 'Андреев Н. А.'
    #     },
    #     {
    #         'title': 'Наша вторая статья',
    #         'text': 'Полный текст статьи',
    #         'date': '22.03.2020',
    #         'author': 'Агапова А. Н'
    #     }
    # ]

    error = ''

    if request.method == 'POST':
        forma = NewsForm(request.POST)
        if forma.is_valid():
            forma.save()
            return redirect('home')
    else:
        error = 'Ошибка'

    forma = NewsForm()


    data = {
        'news': News.objects.all(),
        'title': 'Главная страница',
        'forma': forma,
        'error': error
    }
    return render(request, 'portal/home.html', data)

def about(request):
    return render(request, 'portal/about.html')

def contacts(request):
    return render(request, 'portal/contacts.html')