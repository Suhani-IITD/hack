# Generated by Django 3.2.23 on 2024-01-10 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_lastemail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sleephrs',
            name='d',
        ),
    ]