# Generated by Django 3.2.5 on 2021-09-06 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0023_alter_donation_donationimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='donationImg',
            field=models.ImageField(upload_to='donate/'),
        ),
    ]