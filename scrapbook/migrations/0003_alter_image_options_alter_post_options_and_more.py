# Generated by Django 4.2.17 on 2025-01-12 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scrapbook', '0002_alter_scrapbook_content_alter_scrapbook_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['post']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on']},
        ),
        migrations.AlterModelOptions(
            name='scrapbook',
            options={'ordering': ['-created_on']},
        ),
        migrations.AlterField(
            model_name='post',
            name='scrapbook',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='scrapbook.scrapbook'),
        ),
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Private'), (2, 'Public')], default=0),
        ),
    ]
