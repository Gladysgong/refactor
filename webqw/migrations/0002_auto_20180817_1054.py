# Generated by Django 2.1 on 2018-08-17 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webqw', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='debug',
            old_name='req_text',
            new_name='query',
        ),
        migrations.RemoveField(
            model_name='debug',
            name='reqtype',
        ),
    ]