# Generated by Django 4.1.4 on 2022-12-20 08:46

import book.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0014_rename_name_beeline_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cv_Attachment',
            field=models.FileField(blank=True, null=True, upload_to=book.models.upload_path),
        ),
    ]
