# Generated by Django 4.0.4 on 2022-05-09 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_entriestime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entriestime',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='entriestime',
            name='time',
            field=models.TimeField(),
        ),
    ]
