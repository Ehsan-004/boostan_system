# Generated by Django 5.0.2 on 2024-07-11 16:45

import member.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0011_score_student_alter_score_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='score',
            field=models.IntegerField(default=0, validators=[member.models.score_validator]),
        ),
    ]
