# Generated by Django 5.0 on 2024-06-20 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personel', '0011_rename_icon_project_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personelknowledge',
            name='definition',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='definition',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]