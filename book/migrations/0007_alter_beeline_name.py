# Generated by Django 4.1.4 on 2022-12-19 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_rename_jd_upload_beeline_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beeline',
            name='name',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]