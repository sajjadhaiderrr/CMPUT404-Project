# Generated by Django 2.1.5 on 2019-03-04 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_connection'),
    ]

    operations = [
        migrations.AddField(
            model_name='connection',
            name='starting_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
