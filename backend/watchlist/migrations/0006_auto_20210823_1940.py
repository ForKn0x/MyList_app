# Generated by Django 3.2.6 on 2021-08-23 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0005_review_review_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='avgrating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='num_rating',
            field=models.IntegerField(default=0),
        ),
    ]
