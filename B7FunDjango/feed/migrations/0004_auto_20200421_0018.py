# Generated by Django 2.2.11 on 2020-04-20 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_auto_20200415_2054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='elderly_social_club',
            old_name='Address',
            new_name='address',
        ),
    ]