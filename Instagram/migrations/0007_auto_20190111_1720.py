# Generated by Django 2.0.5 on 2019-01-11 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instagram', '0006_auto_20190111_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
