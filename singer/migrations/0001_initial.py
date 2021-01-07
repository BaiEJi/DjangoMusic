
# Generated by Django 2.0 on 2021-01-05 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('singer_id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('singer_name', models.CharField(max_length=45, verbose_name='姓名')),
                ('singer_type', models.CharField(max_length=45, verbose_name='类型')),
                ('singer_masterwork', models.CharField(max_length=45, verbose_name='代表作')),
                ('singer_sex', models.CharField(max_length=45, verbose_name='性别')),
                ('song_nums', models.CharField(max_length=45, verbose_name='歌曲数')),
                ('singer_img', models.CharField(max_length=45, verbose_name='照片')),
            ],
            options={
                'verbose_name': '歌手信息',
                'verbose_name_plural': '歌手信息',
            },
        ),
    ]
