# Generated by Django 2.0.13 on 2020-03-14 05:27

from django.db import migrations, models
import mouni.models


class Migration(migrations.Migration):

    dependencies = [
        ('mouni', '0015_auto_20200313_1015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='skill',
        ),
        migrations.AlterField(
            model_name='exam',
            name='skillType',
            field=models.CharField(max_length=20, validators=[mouni.models.validate_fields]),
        ),
        migrations.AlterField(
            model_name='exam',
            name='subject',
            field=models.CharField(max_length=20, validators=[mouni.models.validate_fields]),
        ),
    ]
