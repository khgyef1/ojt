# Generated by Django 3.2.5 on 2021-07-28 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ojt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
