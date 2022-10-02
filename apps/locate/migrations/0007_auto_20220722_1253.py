# Generated by Django 3.2.4 on 2022-07-22 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locate', '0006_auto_20220713_0739'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='latitude',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='longitude',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='operating_hours',
            field=models.TextField(blank=True, null=True),
        ),
    ]