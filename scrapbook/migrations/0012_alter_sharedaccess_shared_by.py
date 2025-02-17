# Generated by Django 4.2.17 on 2025-01-22 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scrapbook', '0011_alter_sharedaccess_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharedaccess',
            name='shared_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shared_accesses_shared_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
