# Generated by Django 3.1.6 on 2021-03-09 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Restaurant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant'),
        ),
    ]
