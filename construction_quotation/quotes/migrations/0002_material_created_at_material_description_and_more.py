# Generated by Django 5.1.2 on 2024-11-02 13:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='material',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='material',
            name='unit',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='material',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]