from django.shortcuts import render
from index.models import *
from .models import *
def singerView(request):
    # 搜索歌手
    # search_song = Dynamic.objects.select_related('song').order_by('-dynamic_search').all()[:4]
    # 歌手分类列表
    All_list = Singer.objects.values('singer_type').distinct()
    # 歌曲列表信息
    singer_type = request.GET.get('type', '')
    if singer_type:
        singer_info = SingerDynamic.objects.select_related('singer').filter(singer__singer_type=singer_type).order_by('-singer_plays').all()[:10]
    else:
        singer_info = SingerDynamic.objects.select_related('singer').order_by('-singer_plays').all()[:10]
    return render(request, 'singer.html', locals())



# 通用视图
from django.views.generic import ListView
class SingerRankingList(ListView):
    # context_object_name设置Html模版的某一个变量名称
    context_object_name = 'singer_info'
    # 设定模版文件
    template_name = 'singer.html'
    # 查询变量singer_info的数据
    def get_queryset(self):
        # 获取请求参数
        singer_type = self.request.GET.get('type', '')
        if singer_type:
            singer_info = SingerDynamic.objects.select_related('singer').filter(singer__singer_type=singer_type).order_by('-singer_plays').all()[:10]
        else:
            singer_info = SingerDynamic.objects.select_related('singer').order_by('-singer_plays').all()[:10]
        return singer_info

    # 添加其他变量
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 搜索歌曲
        # context['search_song'] = Dynamic.objects.select_related('song').order_by('-dynamic_search').all()[:4]
        # 所有歌曲分类
        context['All_list'] = Singer.objects.values('singer_type').distinct()
        return context
