# Generated by Django 3.1.7 on 2021-03-25 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_in',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='booking',
            name='check_out',
            field=models.DateField(),
        ),
    ]