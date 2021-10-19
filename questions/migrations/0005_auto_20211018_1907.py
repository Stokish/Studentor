# Generated by Django 3.2.6 on 2021-10-18 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20211017_1427'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.AlterField(
            model_name='post',
            name='question',
            field=models.TextField(verbose_name='Вопрос и его детали'),
        ),
        migrations.AlterField(
            model_name='post',
            name='subject',
            field=models.CharField(max_length=100, verbose_name='Название вопроса'),
        ),
    ]
