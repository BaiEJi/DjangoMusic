from django.urls import path
from . import views
urlpatterns = [
    path('', views.message_view, name='message'),

    # 留言管理按钮
    path('messagebutton1', views.message_admin),

    # 点赞
    path('messagegood', views.message_good)
]