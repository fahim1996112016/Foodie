# Generated by Django 3.1.6 on 2021-03-09 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deliver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nidNo', models.IntegerField()),
                ('profilePicture', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
