# Generated by Django 4.1.3 on 2023-06-16 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0006_remove_stock_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='date2',
            new_name='date',
        ),
    ]