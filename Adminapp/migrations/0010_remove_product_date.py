# Generated by Django 3.2.24 on 2024-04-16 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0009_alter_product_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='date',
        ),
    ]
