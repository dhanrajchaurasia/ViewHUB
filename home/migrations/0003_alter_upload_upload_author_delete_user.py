# Generated by Django 4.0.3 on 2022-10-26 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_remove_upload_tag_remove_upload_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='upload_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
