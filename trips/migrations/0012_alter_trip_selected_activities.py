# Generated by Django 5.2 on 2025-04-28 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0011_alter_trip_selected_activities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='selected_activities',
            field=models.JSONField(blank=True, default=list, null=True),
        ),
    ]
