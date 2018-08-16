# Generated by Django 2.0.1 on 2018-08-15 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fanyi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GpuMonitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.CharField(default='', max_length=50)),
                ('end_time', models.CharField(default='', max_length=50)),
                ('user', models.CharField(max_length=50)),
                ('status', models.IntegerField(default=0)),
                ('monitorip', models.CharField(default='', max_length=500)),
                ('monitoruser', models.CharField(default='', max_length=500)),
                ('monitorpassw', models.CharField(default='', max_length=500)),
                ('gpumem', models.TextField(default='')),
                ('gpumemused', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(db_index=True)),
                ('user', models.CharField(default='', max_length=500)),
                ('passw', models.CharField(default='', max_length=500)),
                ('status', models.IntegerField(default=0)),
                ('runningPID', models.CharField(default='', max_length=20)),
                ('gpuid', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='gpumonitor',
            name='h',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fanyi.Host'),
        ),
    ]
