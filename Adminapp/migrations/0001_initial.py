# Generated by Django 3.2.24 on 2024-03-04 09:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('HR', 'HR'), ('Accountant', 'Accountant'), ('Manager', 'Manager'), ('Supervisor', 'Supervisor'), ('Customer_care', 'Customer_care')], max_length=20)),
                ('state', models.CharField(choices=[('Oyo', 'Oyo'), ('Osun', 'Osun'), ('Ogun', 'Ogun'), ('Lagos', 'Lagos')], max_length=20)),
                ('marital_status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Complicated', 'Complicated')], max_length=20)),
                ('Phone_number', models.IntegerField(max_length=11, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
