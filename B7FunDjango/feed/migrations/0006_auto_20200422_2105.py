# Generated by Django 2.2.11 on 2020-04-22 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_auto_20200421_0019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='community_centers',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='community_centers',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='dog_gardens',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='playgrounds',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='sport_facilities',
            old_name='Name',
            new_name='name',
        ),
    ]
