# Generated by Django 3.1.2 on 2021-03-18 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0007_auto_20210317_2106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ability',
            name='effect',
        ),
        migrations.AddField(
            model_name='ability',
            name='_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
