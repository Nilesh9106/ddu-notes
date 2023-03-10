# Generated by Django 4.1.7 on 2023-02-18 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_userprofile_profilepic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='college',
            name='address',
        ),
        migrations.RemoveField(
            model_name='college',
            name='website',
        ),
        migrations.AddField(
            model_name='college',
            name='domain',
            field=models.CharField(default='ddu.ac.in', max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='college',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.college'),
        ),
    ]
