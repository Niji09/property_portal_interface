# Generated by Django 2.0 on 2018-03-19 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property_portal', '0004_auto_20180318_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='balconies',
            field=models.CharField(choices=[('', 'Select Balcony'), ('1', '1 Balcony'), ('2', '2 Balconies'), ('3', '3 Balconies'), ('4', '4 Balconies')], default='Not Available', max_length=5),
        ),
        migrations.AlterField(
            model_name='buy',
            name='bathroom',
            field=models.CharField(choices=[('', 'Select bathroom'), ('1', '1 Bathroom'), ('2', '2 Bathroom'), ('3', '3 Bathroom'), ('4', '4 Bathroom')], default='1 Bathroom', max_length=5),
        ),
        migrations.AlterField(
            model_name='buy',
            name='city',
            field=models.CharField(choices=[('', 'Select City'), ('DL', 'Delhi'), ('MB', 'Mumbai'), ('KK', 'Kolkata'), ('CN', 'Channai'), ('ND', 'Noida'), ('GD', 'Gurugram'), ('DN', 'Dehradun'), ('BL', 'Bangluru'), ('PN', 'Pune')], default='Select City', max_length=5),
        ),
        migrations.AlterField(
            model_name='buy',
            name='furnished_state',
            field=models.CharField(choices=[('', 'Select Furnished state'), ('NF', 'Not Furnished'), ('SF', 'Semi-Furnished'), ('FF', 'Full Furnished')], default='Not Furnished', max_length=5),
        ),
        migrations.AlterField(
            model_name='buy',
            name='parking',
            field=models.CharField(choices=[('', 'Select Parking'), ('AVC', 'Available, Closed'), ('AVO', 'Available, Open'), ('NAV', 'Not Available')], default='Not Available', max_length=5),
        ),
        migrations.AlterField(
            model_name='buy',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
        migrations.AlterField(
            model_name='buy',
            name='property_for',
            field=models.CharField(choices=[('', 'Select Property For'), ('RES', 'Residential'), ('COM', 'Commercial')], default='Select Property for', max_length=5),
        ),
        migrations.AlterField(
            model_name='buy',
            name='property_type',
            field=models.CharField(choices=[('', 'Select Property Type'), ('1B', '1 BHK'), ('2B', '2 BHK'), ('3B', '3 BHK'), ('4B', '4 BHK'), ('5B', '5 BHK'), ('6B', '6 BHK')], default='Select property_type', max_length=5),
        ),
        migrations.AlterField(
            model_name='buy',
            name='user_info',
            field=models.CharField(choices=[('', 'Select User'), ('OWN', 'Owner'), ('AGN', 'Agent')], default='Select User', max_length=5),
        ),
        migrations.AlterField(
            model_name='rent',
            name='balconies',
            field=models.CharField(choices=[('', 'Select Balcony'), ('1', '1 Balcony'), ('2', '2 Balconies'), ('3', '3 Balconies'), ('4', '4 Balconies')], max_length=5),
        ),
        migrations.AlterField(
            model_name='rent',
            name='bathroom',
            field=models.CharField(choices=[('', 'Select bathroom'), ('1', '1 Bathroom'), ('2', '2 Bathroom'), ('3', '3 Bathroom'), ('4', '4 Bathroom')], max_length=5),
        ),
        migrations.AlterField(
            model_name='rent',
            name='city',
            field=models.CharField(choices=[('', 'Select City'), ('DL', 'Delhi'), ('MB', 'Mumbai'), ('KK', 'Kolkata'), ('CN', 'Channai'), ('ND', 'Noida'), ('GD', 'Gurugram'), ('DN', 'Dehradun'), ('BL', 'Bangluru'), ('PN', 'Pune')], max_length=5),
        ),
        migrations.AlterField(
            model_name='rent',
            name='furnished_state',
            field=models.CharField(choices=[('', 'Select Furnished state'), ('NF', 'Not Furnished'), ('SF', 'Semi-Furnished'), ('FF', 'Full Furnished')], max_length=5),
        ),
        migrations.AlterField(
            model_name='rent',
            name='parking',
            field=models.CharField(choices=[('', 'Select Parking'), ('AVC', 'Available, Closed'), ('AVO', 'Available, Open'), ('NAV', 'Not Available')], max_length=5),
        ),
        migrations.AlterField(
            model_name='rent',
            name='property_for',
            field=models.CharField(choices=[('', 'Select Property For'), ('RES', 'Residential'), ('COM', 'Commercial')], max_length=5),
        ),
        migrations.AlterField(
            model_name='rent',
            name='property_type',
            field=models.CharField(choices=[('', 'Select Property Type'), ('1B', '1 BHK'), ('2B', '2 BHK'), ('3B', '3 BHK'), ('4B', '4 BHK'), ('5B', '5 BHK'), ('6B', '6 BHK')], max_length=5),
        ),
        migrations.AlterField(
            model_name='rent',
            name='user_info',
            field=models.CharField(choices=[('', 'Select User'), ('OWN', 'Owner'), ('AGN', 'Agent')], max_length=5),
        ),
    ]
