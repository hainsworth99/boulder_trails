# Generated by Django 3.1.4 on 2020-12-17 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trails', '0002_auto_20201217_0446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trailsegment',
            name='measured_feet',
            field=models.FloatField(null=True),
        ),
    ]
