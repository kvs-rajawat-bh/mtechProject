# Generated by Django 2.0.5 on 2019-01-11 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Instagram', '0005_userinfo_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='userinfo',
            name='profile_pic',
            field=models.ImageField(default='null', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Instagram.UserInfo'),
        ),
    ]
