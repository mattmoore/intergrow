# Generated by Django 2.2.5 on 2020-03-08 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TeamWork', '0012_auto_20200227_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamgoal',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teamgoal',
            name='is_inprogress',
            field=models.BooleanField(default=True),
        ),
    ]
