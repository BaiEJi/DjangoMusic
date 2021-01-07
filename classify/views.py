from django.shortcuts import render

# Create your views here.
from index.models import *

def classifyView(request):
    # 搜索歌曲
    search_song = Dynamic.objects.select_related('song').order_by('-dynamic_search').all()
    # 歌曲分类列表
    All_list = Song.objects.values('song_type').distinct()
    # 歌曲列表信息
    song_type = request.GET.get('type', '')
    if song_type:
        song_info = Dynamic.objects.select_related('song').filter(song__song_type=song_type).order_by('-dynamic_plays').all()
    else:
        song_info = Dynamic.objects.select_related('song').order_by('-dynamic_plays').all()
    return render(request, 'classify.html', locals())