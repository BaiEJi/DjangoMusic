"""music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
urlpatterns = [

    # 歌手排行榜
    path('', views.singerView, name='singer'),
    
    #表单
    path('.list', views.SingerRankingList.as_view(), name='singerRankingList'),
    
    #歌手主页
    path('detail/<str:singer_name>.html', views.singerDetailView, name='singerDetials'),
    
    # 表单
    path('.info', views.SingerInfoList.as_view(), name='singerInfo'),

    #关注按钮
    # path('followbutton', views.singerfollow, name='follow'),
]