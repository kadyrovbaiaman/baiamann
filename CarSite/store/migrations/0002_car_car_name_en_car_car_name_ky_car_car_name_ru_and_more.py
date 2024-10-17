# Generated by Django 4.2.16 on 2024-10-17 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_name_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='car_name_ky',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='car_name_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='description_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='description_ru',
            field=models.TextField(null=True),
        ),
    ]
