# Generated by Django 4.1.4 on 2022-12-19 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_profile_prodapt_poc_profile_prodapt_practice'),
    ]

    operations = [
        migrations.AddField(
            model_name='beeline',
            name='jd_upload',
            field=models.FileField(default=False, upload_to=''),
        ),
    ]
