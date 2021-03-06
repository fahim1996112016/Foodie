# Generated by Django 3.1.6 on 2021-03-06 11:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Restaurant_name', models.CharField(max_length=100)),
                ('Restaurant_password', models.CharField(max_length=50)),
                ('Restaurant_address', models.TextField(max_length=200)),
                ('Restaurant_email', models.EmailField(max_length=62)),
                ('Restaurant_description', models.TextField(max_length=200)),
                ('Restaurant_phoneNo', models.CharField(max_length=20)),
                ('Restaurant_accountCreated', models.DateTimeField(auto_now_add=True)),
                ('Restaurant_categories', models.CharField(max_length=100)),
                ('Restaurant_rating', models.FloatField(default=1.0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
            ],
        ),
    ]
