# Generated by Django 4.1.3 on 2023-06-25 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='due',
        ),
        migrations.RemoveField(
            model_name='order',
            name='paid',
        ),
    ]