# Generated by Django 3.1.6 on 2021-03-25 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_auto_20210322_0519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.item'),
        ),
    ]
