# Generated by Django 3.0.7 on 2020-09-10 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='日期')),
                ('present_statu', models.CharField(default='正常', max_length=10, verbose_name='出勤状态')),
                ('comment', models.CharField(default='', max_length=100, verbose_name='备注')),
                ('management', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.Management')),
            ],
            options={
                'db_table': 'timebook',
            },
        ),
    ]
