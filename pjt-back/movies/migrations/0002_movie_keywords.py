# Generated by Django 2.2.7 on 2019-11-28 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='keywords',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]