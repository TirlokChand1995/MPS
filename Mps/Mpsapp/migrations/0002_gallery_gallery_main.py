# Generated by Django 4.2.2 on 2023-06-16 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mpsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gal', models.ImageField(upload_to='static')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery_main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gal_main', models.ImageField(upload_to='static')),
            ],
        ),
    ]