# Generated by Django 5.0.1 on 2024-01-19 19:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_alter_advertisement_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='ratings',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='comment',
            name='ad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='ads.advertisement'),
        ),
    ]
