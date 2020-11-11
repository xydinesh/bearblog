# Generated by Django 3.0.7 on 2020-11-03 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0025_auto_20201029_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blocked',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='blog',
            name='favicon',
            field=models.CharField(default='🐼', max_length=2),
        ),
    ]