# Generated by Django 4.2.3 on 2023-11-26 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_alter_news_options_alter_news_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='views',
            field=models.IntegerField(default=1, verbose_name='Просмотры'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='Название статьи'),
        ),
    ]