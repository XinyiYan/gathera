# Generated by Django 3.0.5 on 2020-12-11 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200612_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='max_number_of_judgments_reached',
            field=models.BooleanField(default=False),
        ),
    ]