# Generated by Django 5.1.2 on 2024-10-27 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_custonusers'),
    ]

    operations = [
        migrations.AddField(
            model_name='custonusers',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
