# Create your views here.
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.http import Http404
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from .models import *
import time


# Create your views here .
def index(request):
    return HttpResponse("Hello world")


# 显示留言
def message_view(request):
    # 新增留言
    if request.method == 'POST':
        message_text = request.POST.get('message', '')
        if request.user.username:
            message_user = request.user.username
        else:
            message_user = 'Anonymous'

        if message_text:
            message = Message()
            message.message_text = message_text
            message.message_user = message_user
            message.message_date = time.strftime('%Y-%m-%d %H:%M:%S', \
                                                 time.localtime(time.time()))
            message.save()

        return redirect('/message')

    # 进入留言页面
    else:
        message_all = Message.objects.order_by('message_id')
        page = int(request.GET.get('page', 1))

        # 每页显示的留言条数
        paginator = Paginator(message_all, 8)

        try:
            contacts = paginator.page(page)

        # 避免出现非整数页码
        except PageNotAnInteger:
            contacts = paginator.page(1)

        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)

        return render(request, 'message.html', locals())


# 管理留言
def message_admin(request):
    # 根据是否登录以及用户类别 做出不同的动作
    if request.user.username:
        if request.user.username == 'superuser':
            return redirect('http://127.0.0.1:8000/admin/message/message/')

        else:
            messages.warning(request, '只有超级用户有资格管理留言！')
            # return HttpResponse('只有超级用户有资格管理留言！')
            return redirect('/message/')

    else:
        # return HttpResponse('请登录超级用户账号')
        messages.warning(request, '请登录超级用户账号')
        return redirect('/message/')


# 留言点赞
@csrf_exempt
def message_good(request):
    # 点赞的留言序号
    if request.method == 'POST':
        pass

    message_id = request.POST
    print(message_id)
    message_id = int(list(message_id.keys())[0])

    # 更改数据库
    obj = Message.objects.get(message_id=message_id)
    like = obj.message_like
    like = like + 1
    obj.message_like = like
    obj.save()

    return redirect('/message')


# 搜索留言
def searchview(request, page):
    # return HttpResponse('hello')
    if request.method == 'GET':
        # 搜索评论
        search_message = Message.objects.all()

        # 获取搜索内容
        kword = request.session.get('kword', '')

        if kword:
            # Q or
            message_info = Message.objects.values('message_like', 'message_id', 'message_text', 'message_user'). \
                filter(Q(message_text__icontains=kword) | Q(message_user=kword) | Q(message_date__icontains=kword)). \
                order_by('message_like').all()

        # 返回点赞数最高的50条
        else:
            message_info = Message.objects.values('message_like', 'message_id', 'message_text', 'message_user'). \
                               order_by('message_like').all()[:50]

        # page
        paginator = Paginator(message_info, 8)

        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)

        return render(request, 'messagesearch.html', locals())

    else:
        # 处理post请求，重定向搜索页面
        request.session['kword'] = request.POST.get('kword', '')
        return redirect('1.html')


# 设置404、500错误状态码
from index import views
handler404 = views.page_not_found
handler500 = views.page_not_found
