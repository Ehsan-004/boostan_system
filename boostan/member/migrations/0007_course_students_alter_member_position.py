# Generated by Django 5.0.2 on 2024-07-10 17:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0006_alter_member_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='member.student'),
        ),
        migrations.AlterField(
            model_name='member',
            name='position',
            field=models.CharField(choices=[('student', 'student'), ('employee', 'employee'), ('teacher', 'teacher'), ('personnel', 'personnel'), ('admin', 'admin')], default='personnel', max_length=10),
        ),
    ]