# Generated by Django 3.0.4 on 2021-11-16 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addbook',
            name='genres',
            field=models.CharField(choices=[('Fiction', 'Fiction'), ('Nonfiction', 'Nonfiction'), ('Romance', 'Romance'), ('Crime and Thriller', 'Crime and Thriller'), ('Religious', 'Religious'), ('Self-help', 'Self-help'), ('Sci-fi', 'Sci-fi'), ('Poetry', 'Poetry')], default='', max_length=20, verbose_name='Book Genres'),
        ),
    ]
