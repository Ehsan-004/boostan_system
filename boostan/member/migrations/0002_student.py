# Generated by Django 5.0.2 on 2024-06-28 11:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=10)),
                ('passed_terms', models.IntegerField(default=0)),
                ('member_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='member.member')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
                'db_table': 'students',
            },
        ),
    ]