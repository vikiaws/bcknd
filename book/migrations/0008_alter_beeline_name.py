# Generated by Django 4.1.4 on 2022-12-19 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_alter_beeline_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beeline',
            name='name',
            field=models.FileField(default=False, upload_to=''),
        ),
    ]