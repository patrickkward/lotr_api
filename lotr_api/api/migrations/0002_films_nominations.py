# Generated by Django 2.2.6 on 2019-10-15 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='films',
            name='nominations',
            field=models.CharField(default='', max_length=200),
        ),
    ]