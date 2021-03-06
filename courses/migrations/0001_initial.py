# Generated by Django 3.1.2 on 2020-10-09 01:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('cover', models.ImageField(blank=True, upload_to='covers/')),
            ],
        ),
    ]
