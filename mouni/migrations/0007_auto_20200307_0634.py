# Generated by Django 2.0.13 on 2020-03-07 01:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mouni', '0006_auto_20200306_1053'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultPerExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.PositiveIntegerField(editable=False)),
            ],
        ),
        migrations.AlterField(
            model_name='exam',
            name='teacher',
            field=models.CharField(editable=False, max_length=20),
        ),
        migrations.AddField(
            model_name='resultperexam',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='mouni.Exam'),
        ),
        migrations.AddField(
            model_name='resultperexam',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
