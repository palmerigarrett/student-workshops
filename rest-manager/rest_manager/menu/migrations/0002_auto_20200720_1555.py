# Generated by Django 3.0.8 on 2020-07-20 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='created',
            field=models.DateField(default='2020-07-20'),
        ),
    ]
