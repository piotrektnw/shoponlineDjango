# Generated by Django 3.1.6 on 2021-03-25 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0024_auto_20210325_2103'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='item',
            new_name='item_id',
        ),
    ]
