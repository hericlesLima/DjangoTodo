# Generated by Django 4.0.6 on 2022-07-04 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]