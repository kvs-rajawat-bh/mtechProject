# Generated by Django 2.0.5 on 2019-01-11 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instagram', '0002_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('username', models.CharField(max_length=1000)),
                ('password', models.CharField(max_length=1000)),
            ],
        ),
        migrations.RenameField(
            model_name='login',
            old_name='Password',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='login',
            old_name='Username',
            new_name='username',
        ),
    ]
