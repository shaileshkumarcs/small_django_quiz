# Generated by Django 2.0.1 on 2018-06-17 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_user_is_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_studentdetails',
            field=models.BooleanField(default=False),
        ),
    ]