# Generated by Django 4.2.17 on 2025-01-15 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapbook', '0007_alter_post_image_alter_scrapbook_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
    ]
