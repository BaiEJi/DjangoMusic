from django.urls import path
from . import views
urlpatterns = [
    path('', views.messageview, name='message'),

    # 留言管理按钮
    path('messagebutton1', views.messageAdmin)
]