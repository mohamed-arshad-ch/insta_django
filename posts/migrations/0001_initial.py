# Generated by Django 5.0.2 on 2024-02-21 11:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchedUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'searched_users',
            },
        ),
        migrations.CreateModel(
            name='InstaData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('json_data', models.JSONField()),
                ('file_name', models.CharField(max_length=200)),
                ('files_array', models.JSONField()),
                ('flag', models.BooleanField(default=True)),
                ('related_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.searcheduser')),
            ],
            options={
                'db_table': 'insta_data',
            },
        ),
    ]
