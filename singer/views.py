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
        singer_info = SingerDynamic.objects.select_related('singer').filter(singer__singer_type=singer_type).order_by('-singer_plays').all()[:15]
    else:
        singer_info = SingerDynamic.objects.select_related('singer').order_by('-singer_plays').all()[:15]
    return render(request, 'singer.html', locals())

def singerDetailView(request,singer_name):
    # 搜索歌手
    search_song = Dynamic.objects.select_related('song').order_by('-dynamic_search').all()[:4]
    # 歌曲分类列表
    singer_list = Song.objects.values('song_type').filter(song_singer=str(singer_name)).distinct()
    # if All_list:
    #     song_list = Song.objects.select_related('song_singer').filter(singer__singer_name=str(singer_name)).order_by('-dynamic_plays').all()[:15]
    # else:
    #     song_list = Song.objects.select_related('song_singer').order_by('-dynamic_plays').all()[:15]
    # 歌手信息
    singer_detail = Singer.objects.get(singer_name=str(singer_name))
    # singer_name = request.GET.get('name', '')
    if singer_detail:
        song_info = Dynamic.objects.select_related('song').filter(song__song_singer=str(singer_name)).order_by('-dynamic_plays').all()[:15]
    else:
        song_info = Dynamic.objects.select_related('song').order_by('-dynamic_plays').all()[:15]
    return render(request, 'info.html', locals())

# 歌手排行榜通用视图
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
            singer_info = SingerDynamic.objects.select_related('singer').filter(singer__singer_type=singer_type).order_by('-singer_plays').all()[:15]
        else:
            singer_info = SingerDynamic.objects.select_related('singer').order_by('-singer_plays').all()[:15]
        return singer_info

    # 添加其他变量
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 搜索歌曲
        # context['search_song'] = Dynamic.objects.select_related('song').order_by('-dynamic_search').all()[:4]
        # 所有歌曲分类
        context['All_list'] = Singer.objects.values('singer_type').distinct()
        return context

#歌手主页视图
class SingerInfoList(ListView):
    # context_object_name设置Html模版的某一个变量名称
    context_object_name = 'singer_detail'
    # 设定模版文件
    template_name = 'info.html'
    # 查询变量singer_detail的数据
    def get_queryset(self):
        # 获取请求参数
        singer_type = self.request.GET.get('type', '')
        if singer_type:
            singer_info = SingerDynamic.objects.select_related('singer').filter(singer__singer_type=singer_type).order_by('-singer_plays').all()[:15]
        else:
            singer_info = SingerDynamic.objects.select_related('singer').order_by('-singer_plays').all()[:15]
        return singer_info

    # 添加其他变量
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 搜索歌曲
        # context['search_song'] = Dynamic.objects.select_related('song').order_by('-dynamic_search').all()[:4]
        # 所有歌曲分类
        context['All_list'] = Singer.objects.values('singer_type').distinct()
        return context