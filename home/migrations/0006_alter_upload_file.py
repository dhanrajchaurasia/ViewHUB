# Generated by Django 4.0.3 on 2022-10-28 14:24

from django.db import migrations, models
import home.validators


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_upload_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='file',
            field=models.FileField(null=True, upload_to='videos/', validators=[home.validators.fileSize]),
        ),
    ]
