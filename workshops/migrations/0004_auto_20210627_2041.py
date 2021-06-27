# Generated by Django 3.2.4 on 2021-06-27 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshops', '0003_auto_20210627_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workshop',
            name='zoom_password',
        ),
        migrations.AddField(
            model_name='workshop',
            name='zoom_passcode',
            field=models.CharField(blank=True, help_text='Zoom passcode to the workshop.', max_length=200),
        ),
    ]