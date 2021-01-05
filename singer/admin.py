from django.contrib import admin
from .models import *


# Register your models here.
# 在后台管理留言

@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    # 显示字段
    list_display = ['singer_id', 'singer_name', 'singer_type', \
                    'singer_masterwork', 'singer_sex', 'song_nums']

    # 设置可搜索的字段并在Admin 后台数据生成搜索框，
    search_fields = ['singer_id', 'singer_name', 'singer_type', \
                    'singer_masterwork', 'singer_sex', 'song_nums']

    # 设置排序方式
    ordering = ['singer_id']

    # 在添加新数据时，设置可添加数据的字段
    fields = ['singer_name', 'singer_type', 'singer_masterwork', \
            'singer_sex', 'song_nums']


