# Generated by Django 3.1.7 on 2021-03-25 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_auto_20210325_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='rate',
            field=models.IntegerField(default=1000),
            preserve_default=False,
        ),
    ]
