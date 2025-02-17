# Generated by Django 4.2.17 on 2025-01-22 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapbook', '0010_sharedaccess'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='sharedaccess',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='sharedaccess',
            constraint=models.UniqueConstraint(fields=('user', 'scrapbook', 'post'), name='unique_shared_access'),
        ),
    ]
