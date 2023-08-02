# Generated by Django 4.1.2 on 2022-10-31 07:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0010_upload_private_alter_upload_tag_alter_upload_title"),
    ]

    operations = [
        migrations.RenameField(
            model_name="upload",
            old_name="favorite",
            new_name="isfav",
        ),
        migrations.RemoveField(
            model_name="upload",
            name="id",
        ),
        migrations.AddField(
            model_name="upload",
            name="postId",
            field=models.IntegerField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]