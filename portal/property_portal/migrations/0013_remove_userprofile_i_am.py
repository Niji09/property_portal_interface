# Generated by Django 2.0 on 2018-03-26 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property_portal', '0012_auto_20180321_2340'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='i_am',
        ),
    ]
