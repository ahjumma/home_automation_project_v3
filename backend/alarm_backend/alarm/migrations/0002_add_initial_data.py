# Generated by Django 2.2.4 on 2019-08-12 01:51

from django.db import migrations, models
import django.db.models.deletion


def add_alarm_status(apps, schema_editor):
    AlarmStatus = apps.get_model("alarm", "AlarmStatus")
    AlarmStatus(is_active=True).save()


def delete_alarm_status(apps, schema_editor):
    AlarmStatus = apps.get_model("alarm", "AlarmStatus")
    for obj in AlarmStatus.objects.all():
        obj.delete()


def add_commands(apps, schema_editor):
    Command = apps.get_model("alarm", "Command")
    Command(name="testing script", target_file="test_script.py").save()
    Command(name="sunlight simulation", target_file="sunlight_simulation.py").save()


def delete_commands(apps, schema_editor):
    Command = apps.get_model("alarm", "Command")
    for obj in Command.objects.all():
        obj.delete()


class Migration(migrations.Migration):

    dependencies = [
        ("alarm", "0001_initial")
    ]

    operations = [
        migrations.RunPython(
            add_alarm_status,
            reverse_code=delete_alarm_status
        ),
        migrations.RunPython(
            add_commands,
            reverse_code=delete_commands
        ),
    ]
