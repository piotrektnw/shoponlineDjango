# Generated by Django 3.1.6 on 2021-03-20 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_bid_winner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='startingbid',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=5),
        ),
    ]
