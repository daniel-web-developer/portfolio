# Generated by Django 4.1.7 on 2023-04-14 18:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_project_gitlink_alter_project_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='gitlink',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=datetime.datetime(2023, 4, 14, 18, 2, 29, 321895, tzinfo=datetime.timezone.utc)),
        ),
    ]
