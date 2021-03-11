# Generated by Django 3.1.6 on 2021-03-11 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_restaurant_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='Restaurant_categories',
            new_name='categories',
        ),
        migrations.RenameField(
            model_name='restaurant',
            old_name='Restaurant_description',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='Restaurant_rating',
        ),
    ]
