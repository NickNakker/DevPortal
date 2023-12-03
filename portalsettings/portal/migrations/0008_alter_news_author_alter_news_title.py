# Generated by Django 4.2.3 on 2023-12-03 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0007_alter_tasks_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название статьи'),
        ),
    ]
