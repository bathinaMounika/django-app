# Generated by Django 2.0.13 on 2020-03-05 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mouni', '0004_auto_20200305_1107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='skill',
        ),
        migrations.AddField(
            model_name='question',
            name='skill',
            field=models.CharField(default='addition', max_length=20),
            preserve_default=False,
        ),
    ]
