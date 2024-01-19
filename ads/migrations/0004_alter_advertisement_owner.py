# Generated by Django 5.0.1 on 2024-01-19 17:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_advertisement_status_alter_advertisement_price'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to=settings.AUTH_USER_MODEL),
        ),
    ]
