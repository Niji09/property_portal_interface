# Generated by Django 2.0 on 2018-03-20 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property_portal', '0008_auto_20180320_0831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rent',
            name='w_e_charges',
        ),
    ]
