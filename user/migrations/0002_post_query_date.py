# Generated by Django 4.1.4 on 2023-02-21 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_query',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
