# Generated by Django 2.1.1 on 2019-01-20 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_remove_subject_subject_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gradepost',
            name='grade_info',
        ),
    ]