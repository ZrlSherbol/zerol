# Generated by Django 5.1.1 on 2024-10-10 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0003_review_stars'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name=((1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****'))),
        ),
    ]
