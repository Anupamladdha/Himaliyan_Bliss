# Generated by Django 3.1.7 on 2021-08-30 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0010_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.CharField(choices=[], max_length=3),
        ),
    ]
