# Generated by Django 5.0.4 on 2024-04-26 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0002_dish'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='end_period',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='dish',
            name='start_period',
            field=models.DateField(null=True),
        ),
    ]