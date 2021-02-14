# Generated by Django 3.1.6 on 2021-02-12 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_model', models.CharField(max_length=50)),
                ('car_numberplate', models.CharField(max_length=10)),
                ('car_image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('car_sits', models.IntegerField()),
                ('price_per_day', models.ImageField(upload_to='')),
            ],
        ),
    ]