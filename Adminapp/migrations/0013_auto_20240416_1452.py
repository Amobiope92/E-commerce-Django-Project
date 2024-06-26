# Generated by Django 3.2.24 on 2024-04-16 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0012_rename_user_product_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
