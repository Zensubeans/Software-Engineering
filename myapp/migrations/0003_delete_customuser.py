# Generated by Django 5.1.1 on 2024-11-23 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
