# Generated by Django 4.1.5 on 2023-02-08 22:00

from django.db import migrations, models
import thrifty_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('thrifty_app', '0007_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=thrifty_app.models.upload_path),
        ),
    ]
