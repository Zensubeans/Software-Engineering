# Generated by Django 5.1.1 on 2024-12-04 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_qrcodescan'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QRCodeScan',
        ),
    ]