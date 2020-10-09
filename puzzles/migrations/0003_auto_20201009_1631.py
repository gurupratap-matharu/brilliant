# Generated by Django 3.1.2 on 2020-10-09 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puzzles', '0002_auto_20201009_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='puzzle',
            name='intro',
            field=models.TextField(blank=True, verbose_name='Introduction'),
        ),
        migrations.AddField(
            model_name='puzzle',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='puzzle',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
    ]
