# Generated by Django 3.2.4 on 2022-07-12 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locate', '0003_auto_20220712_0959'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='çstate_id',
            new_name='state_id',
        ),
    ]
