# Generated by Django 4.0 on 2022-08-31 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='nome',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
