# Generated by Django 2.2.5 on 2020-02-25 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TeamWork', '0006_auto_20200221_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndividualGoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_discription', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
        migrations.CreateModel(
            name='IndividualGoalProgress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress_description', models.CharField(max_length=300)),
                ('progress_date', models.DateField()),
                ('individual_goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TeamWork.IndividualGoal')),
            ],
        ),
        migrations.AddField(
            model_name='individualgoal',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TeamWork.Employee'),
        ),
    ]