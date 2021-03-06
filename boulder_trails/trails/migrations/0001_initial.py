# Generated by Django 3.1.4 on 2020-12-16 19:46

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrailClosure',
            fields=[
                ('object_id', models.IntegerField(primary_key=True, serialize=False)),
                ('closure_duration', models.CharField(max_length=100, null=True)),
                ('closure_reason', models.CharField(max_length=100, null=True)),
                ('closure_area', models.CharField(max_length=100, null=True)),
                ('trail_status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Trail',
            fields=[
                ('object_id', models.IntegerField(primary_key=True, serialize=False)),
                ('owner', models.CharField(max_length=50, null=True)),
                ('bikes', models.BooleanField()),
                ('trail_type', models.CharField(max_length=50, null=True)),
                ('segment_id', models.CharField(max_length=50, null=True)),
                ('horses', models.BooleanField()),
                ('trail_id', models.IntegerField()),
                ('mileage', models.FloatField()),
                ('measured_feet', models.FloatField()),
                ('trail_name', models.CharField(max_length=100)),
                ('global_id', models.CharField(max_length=100)),
                ('dogs', models.BooleanField()),
                ('st_length', models.FloatField()),
                ('geometry', django.contrib.gis.db.models.fields.LineStringField(srid=4326)),
                ('closure_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trails.trailclosure')),
            ],
        ),
    ]
