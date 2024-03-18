# Generated by Django 4.2.7 on 2024-03-18 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_indexmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='indexpermissionmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('index_name', models.CharField(max_length=50)),
                ('collection_name', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='llmmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('llm', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='llmpermissionmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('index_name', models.CharField(max_length=50)),
                ('collection_name', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
