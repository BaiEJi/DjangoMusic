from django.urls import path
from . import views
urlpatterns = [
    path('', views.message_view, name='message'),

    # 留言管理按钮
    path('messagebutton1', views.message_admin),

    # 点赞
    path('messagegood', views.message_good),

    # 点踩
    path('messagebad', views.message_bad),

    # 点赞
    path('messagegood2', views.message_good2),

    # 点踩
    path('messagebad2', views.message_bad2),

    # 搜索留言
    path('messagesearch/<int:page>.html', views.searchview, name= 'searchmessage') ,

    # 删除
    path('messagedelete', views.message_delete),

    # 删除搜索界面
    path('messagesearchdelete', views.message_search_delete),

    # order
    path('messageorder', views.message_order),
]