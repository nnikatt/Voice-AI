# Generated by Django 4.0 on 2022-01-13 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_alter_dubberapitoken_tokenexpiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dubberapitoken',
            name='expiryTime',
            field=models.DateTimeField(blank=True),
        ),
    ]
