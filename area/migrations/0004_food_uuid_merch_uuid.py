# Generated by Django 5.2.2 on 2025-06-27 16:42

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0003_event_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='uuid',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='merch',
            name='uuid',
            field=models.UUIDField(blank=True, default=uuid.uuid4, editable=False, null=True),
        ),
    ]
