# Generated by Django 5.0.2 on 2024-06-28 11:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=30)),
                ('member_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='member.member')),
            ],
            options={
                'verbose_name': 'Personnel',
                'verbose_name_plural': 'Personnel',
                'db_table': 'personnel',
            },
        ),
    ]
