# Generated by Django 4.1.7 on 2023-02-18 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_note_visibility'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='semester',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profilePic',
            field=models.ImageField(default='/profile/default.png', upload_to='profile/'),
        ),
    ]
