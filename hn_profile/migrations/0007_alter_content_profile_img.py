# Generated by Django 5.0.3 on 2024-03-25 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hn_profile', '0006_user_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='profile_img',
            field=models.URLField(null=True),
        ),
    ]
