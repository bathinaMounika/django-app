# Generated by Django 2.0.13 on 2020-03-11 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mouni', '0013_auto_20200308_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultperexam',
            name='seed',
            field=models.PositiveIntegerField(default=23, editable=False),
            preserve_default=False,
        ),
    ]