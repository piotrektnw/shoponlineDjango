# Generated by Django 3.1.6 on 2021-03-12 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20210311_0454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='item_id',
            field=models.IntegerField(blank=True, default=None),
        ),
    ]
