# Generated by Django 3.1.7 on 2021-04-09 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
