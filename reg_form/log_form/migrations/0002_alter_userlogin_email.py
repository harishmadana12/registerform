# Generated by Django 3.2.3 on 2021-06-20 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlogin',
            name='email',
            field=models.EmailField(max_length=30),
        ),
    ]