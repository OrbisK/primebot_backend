# Generated by Django 3.0.8 on 2022-06-09 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_prime_league', '0036_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]