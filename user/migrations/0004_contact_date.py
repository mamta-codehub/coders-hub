# Generated by Django 4.1.4 on 2023-02-22 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
