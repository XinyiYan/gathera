# Generated by Django 3.0.5 on 2020-10-01 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('judgment', '0005_judgment_other_criteria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='judgment',
            old_name='other_criteria',
            new_name='additional_judging_criteria',
        ),
    ]
