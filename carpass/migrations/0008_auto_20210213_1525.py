# Generated by Django 3.1.6 on 2021-02-13 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpass', '0007_auto_20210213_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='booked_by',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
