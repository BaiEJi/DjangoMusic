from django.apps import AppConfig
import os

# 修改App 在Admin 后台显示的名称
# default_app_config 的值来自apps.py 的类名
default_app_config = 'message.MessageConfig'


# 获取当前App 的命名
def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]


# 重写类IndexConfig
class MessageConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = '留言管理 '
