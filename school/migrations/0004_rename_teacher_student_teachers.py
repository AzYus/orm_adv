# Generated by Django 4.2.4 on 2023-09-03 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_alter_student_id_alter_teacher_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='teacher',
            new_name='teachers',
        ),
    ]
