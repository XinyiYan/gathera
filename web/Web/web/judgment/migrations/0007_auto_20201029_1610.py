# Generated by Django 3.0.5 on 2020-10-29 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('judgment', '0006_auto_20200930_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='judgment',
            name='doc_CAL_snippet',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='judgment',
            name='doc_search_snippet',
            field=models.TextField(blank=True, null=True),
        ),
    ]

