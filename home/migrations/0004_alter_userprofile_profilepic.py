# Generated by Django 4.1.7 on 2023-02-16 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_subject_department_remove_college_admin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profilePic',
            field=models.ImageField(default='profile/default.png', upload_to='profile/'),
        ),
    ]
