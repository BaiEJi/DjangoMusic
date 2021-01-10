# Generated by Django 2.0 on 2021-01-10 06:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('singer', '0004_auto_20210107_2052'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow_time', models.CharField(blank=True, max_length=50, null=True, verbose_name='关注时间')),
                ('singer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='singer.Singer', verbose_name='歌手ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户ID')),
            ],
            options={
                'verbose_name': '关注状态',
                'verbose_name_plural': '关注状态',
            },
        ),
    ]
