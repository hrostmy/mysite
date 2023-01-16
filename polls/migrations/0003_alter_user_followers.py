# Generated by Django 4.1.5 on 2023-01-16 18:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_user_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='followers',
            field=models.ManyToManyField(related_name='follower', to=settings.AUTH_USER_MODEL),
        ),
    ]
