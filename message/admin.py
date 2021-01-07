from django.contrib import admin
from .models import *


# Register your models here.
# 在后台管理留言

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    # 显示字段
    list_display = ['message_id', 'message_text', 'message_user', \
                    'message_date', 'message_like']

    # 设置可搜索的字段并在Admin 后台数据生成搜索框，
    search_fields = ['message_id', 'message_text', 'message_user', \
                     'message_date']

    # 设置排序方式
    ordering = ['message_id']

    # 在添加新数据时，设置可添加数据的字段
    fields = ['message_text', 'message_user', 'message_date']

    # 新增数据条目
    def save_model(self, request, obj, form, change):
        if change:
            # 写日志
            user = request.user
            name = self.model.objects.get(pk=obj.pk).message_user
            text = form.cleaned_data['message_text']
            mid = self.model.objects.get(pk=obj.pk).message_id
            f = open('D:/Django_music_log.txt', 'a')
            f.write('留言序号：' + str(mid) + \
                    '\t用户:' + name + '\n留言内容：' + text + '\n')
            f.close()

        else:
            pass

        # 使用父类的方法
        super(MessageAdmin, self).save_model(request, obj, form, change)
