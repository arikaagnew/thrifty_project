# Generated by Django 4.1.5 on 2023-02-08 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thrifty_app', '0005_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
