# Generated by Django 4.2.8 on 2023-12-22 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_uploadedcontent_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedcontent',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
    ]
