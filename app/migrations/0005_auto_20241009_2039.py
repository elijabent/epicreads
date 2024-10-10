# Generated by Django 3.2.25 on 2024-10-10 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20241006_1908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='book',
            name='author_first',
            field=models.CharField(default='error', max_length=50),
        ),
        migrations.AddField(
            model_name='book',
            name='author_last',
            field=models.CharField(default='error', max_length=50),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover_back',
            field=models.ImageField(default=None, upload_to='covers/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover_front',
            field=models.ImageField(default=None, upload_to='covers/'),
        ),
    ]
