# Generated by Django 3.2.4 on 2022-07-22 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opti', '0002_post_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='video'),
        ),
    ]
