# Generated by Django 3.1.6 on 2021-03-09 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('addToCart', '0002_addtocart_customer'),
        ('dishes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtocart',
            name='Dishes',
            field=models.ManyToManyField(to='dishes.Dishes'),
        ),
    ]