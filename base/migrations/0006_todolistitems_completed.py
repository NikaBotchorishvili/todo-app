# Generated by Django 4.0.6 on 2022-07-27 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolistitems',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]