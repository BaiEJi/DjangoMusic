from django.contrib import admin
from .models import *
# Register your models here.
# 在后台管理留言

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    # 显示字段
    list_display = ['message_id','message_text','message_user',\
                    'message_date', 'message_like' ]