# Create your views here.
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.http import Http404
from index.models import *
from .models import  *
import time


# Create your views here .
def index(request):
    return HttpResponse("Hello world")


def messageview(request):

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
            message.message_date = time.strftime('%Y-%m-%d', \
                                time.localtime(time.time()))
            message.save()

        return redirect('/message')

    else:
        message_all = Message.objects.order_by('message_id')
        page = int(request.GET.get('page', 1))
        paginator = Paginator(message_all, 2)

        try:
            contacts = paginator.page(page)

        except PageNotAnInteger:
            contacts = paginator.page(1)

        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)

        return render(request, 'message.html', locals())