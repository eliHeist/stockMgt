# Generated by Django 4.1.3 on 2023-06-25 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_remove_order_grand_total_remove_order_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_status',
            field=models.FloatField(),
        ),
    ]