# Generated by Django 4.2.2 on 2024-04-16 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_streamuser_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='streamuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]