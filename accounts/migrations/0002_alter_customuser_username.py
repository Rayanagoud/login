# Generated by Django 4.1 on 2023-10-10 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
