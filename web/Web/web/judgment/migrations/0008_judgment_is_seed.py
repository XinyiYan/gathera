# Generated by Django 3.0.5 on 2020-12-12 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judgment', '0007_auto_20201029_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='judgment',
            name='is_seed',
            field=models.BooleanField(default=False),
        ),
    ]