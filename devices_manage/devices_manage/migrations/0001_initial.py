# Generated by Django 3.0.7 on 2020-06-25 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('asset_numbers', models.CharField(max_length=200)),
                ('use_users', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('system_version', models.CharField(max_length=200)),
                ('resolution', models.CharField(max_length=200)),
                ('administrator', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=200)),
                ('update_time', models.DateTimeField()),
                ('is_delete', models.IntegerField(default=0)),
            ],
        ),
    ]
