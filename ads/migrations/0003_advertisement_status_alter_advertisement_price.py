# Generated by Django 5.0.1 on 2024-01-18 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_advertisement_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='status',
            field=models.CharField(choices=[('D', 'Draft'), ('P', 'Pending Approval'), ('A', 'Approved')], default='D', max_length=1),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
