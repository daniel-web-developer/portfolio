# Generated by Django 4.1.7 on 2023-04-14 17:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_article_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=datetime.datetime(2023, 4, 14, 17, 38, 28, 196038, tzinfo=datetime.timezone.utc)),
        ),
    ]