# Generated by Django 2.0.5 on 2019-07-17 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_phones'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(default='a'),
            preserve_default=False,
        ),
    ]