# Generated by Django 4.1.3 on 2023-06-16 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0004_alter_stock_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='date2',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]