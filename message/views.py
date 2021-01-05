# Create your views here.
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.http import Http404
from .models import *
import time


# Create your views here .
def index(request):
    return HttpResponse("Hello world")


# 显示留言
def messageview(request):

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
def messageAdmin(request):

    # 根据是否登录以及用户类别 做出不同的动作
    if request.user.username:
        if request.user.username == 'superuser':
            return redirect('http://127.0.0.1:8000/admin/message/message/')

        else:
            return HttpResponse('只有超级用户有资格管理留言！')

    else:
        return HttpResponse('请登录超级用户账号')