# Generated by Django 3.2.5 on 2021-09-06 03:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecommerce', '0019_auto_20210902_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('donationId', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('dateCreated', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('itemType', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=500)),
                ('donationImg', models.ImageField(upload_to='donation')),
                ('yearPurchased', models.DateField(null=True)),
                ('originalPrice', models.DecimalField(decimal_places=2, max_digits=8)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
