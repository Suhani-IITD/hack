# Generated by Django 3.2.23 on 2024-01-10 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_sleephrs'),
    ]

    operations = [
        migrations.CreateModel(
            name='lastemail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
