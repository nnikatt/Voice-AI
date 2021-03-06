# Generated by Django 4.0 on 2022-01-17 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_alter_dubberapitoken_expirytime'),
    ]

    operations = [
        migrations.AddField(
            model_name='dubberapitoken',
            name='account_id',
            field=models.CharField(blank=True, max_length=600),
        ),
        migrations.AddField(
            model_name='dubberapitoken',
            name='auth_id',
            field=models.CharField(blank=True, max_length=600),
        ),
        migrations.AddField(
            model_name='dubberapitoken',
            name='auth_secret',
            field=models.CharField(blank=True, max_length=600),
        ),
        migrations.AddField(
            model_name='dubberapitoken',
            name='client_id',
            field=models.CharField(blank=True, max_length=600),
        ),
        migrations.AddField(
            model_name='dubberapitoken',
            name='client_secret',
            field=models.CharField(blank=True, max_length=600),
        ),
        migrations.AddField(
            model_name='dubberapitoken',
            name='region',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
