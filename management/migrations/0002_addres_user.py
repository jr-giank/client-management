# Generated by Django 5.0.3 on 2024-03-27 19:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='addres',
            name='user',
            field=models.ForeignKey(blank=True, default=3, max_length=100, on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL, verbose_name='Cliente'),
            preserve_default=False,
        ),
    ]
