# Generated by Django 5.0 on 2024-06-17 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=25, null=True, unique=True)),
                ('definition', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=25, null=True, unique=True)),
                ('definition', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=25, null=True, unique=True)),
                ('definition', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]