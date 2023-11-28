# DevPortal
Project for Dev Contest

# Настройки
Скопируйте файл .env.dist с названием .env и укажите там локальные настройки. Можно ничего не трогать

# Команды для запуска
Установите Docker Desktop и выполните в папке проекта
```shell
docker-compose build
docker-compose up -d
```

# Подготовка проекта
После первого запуска проекта выполните следующие команды в контейнере app для подготовки проекта к работе
```shell
python manage.py migrate
python manage.py collectstatic
```

# Статика
Все статические файлы при работе сервера берутся из каталога *portalsettings/static*
В репозиторий сохранять готовую статику в каталог *portalsettings/static/portal*
Запрашивается статика с фронта по адресу */static/portal*

