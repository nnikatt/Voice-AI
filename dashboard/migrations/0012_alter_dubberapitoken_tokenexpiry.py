# Generated by Django 4.0 on 2022-01-13 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_dubberapitoken_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dubberapitoken',
            name='tokenExpiry',
            field=models.BigIntegerField(),
        ),
    ]