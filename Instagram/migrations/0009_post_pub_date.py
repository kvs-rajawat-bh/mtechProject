# Generated by Django 2.0.5 on 2019-01-12 04:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instagram', '0008_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 12, 10, 17, 48, 399947)),
            preserve_default=False,
        ),
    ]
