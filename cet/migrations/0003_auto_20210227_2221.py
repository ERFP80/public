# Generated by Django 3.1.5 on 2021-02-27 18:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cet', '0002_pendingtransactions_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendingtransactions',
            name='token',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
