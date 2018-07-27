# Generated by Django 2.0 on 2018-03-14 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat_type', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=1000)),
                ('price', models.CharField(max_length=20)),
                ('flat_image', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='BuyDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bedroom', models.CharField(max_length=3)),
                ('bathroom', models.CharField(max_length=3)),
                ('balcony', models.CharField(max_length=3)),
                ('facing', models.CharField(max_length=50)),
                ('parking', models.BooleanField(default=False)),
                ('buy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property_portal.Buy')),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat_type', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=1000)),
                ('price', models.CharField(max_length=20)),
                ('flat_image', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='RentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bedroom', models.CharField(max_length=3)),
                ('bathroom', models.CharField(max_length=3)),
                ('balcony', models.CharField(max_length=3)),
                ('facing', models.CharField(max_length=50)),
                ('parking', models.BooleanField(default=False)),
                ('rent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property_portal.Rent')),
            ],
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat_type', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=1000)),
                ('price', models.CharField(max_length=20)),
                ('flat_image', models.CharField(max_length=2000)),
            ],
        ),
    ]