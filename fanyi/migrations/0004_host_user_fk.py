# Generated by Django 2.0.1 on 2018-08-20 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0003_auto_20180814_1419'),
        ('fanyi', '0003_maneval_manevaldiff'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='user_fk',
            field=models.ForeignKey(default='zhangjingjun', on_delete=django.db.models.deletion.CASCADE, to='rbac.UserInfo', to_field='username'),
            preserve_default=False,
        ),
    ]
