# Generated by Django 4.2.2 on 2023-06-13 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pic', models.ImageField(default='Noimage.jpg', upload_to='static')),
                ('Name', models.CharField(default='', max_length=50)),
                ('Des', models.CharField(default='Teacher', max_length=50)),
                ('Experience', models.IntegerField(default=0)),
            ],
        ),
    ]
