# Generated by Django 2.2 on 2020-03-20 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentusers',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='logsreport',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
