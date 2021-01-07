# 定义表单对象
from django import forms
from .models import *

class ChoiceForm(forms.Form):

    choice_list1 = [(1, '默认'),(2,'用户'),(3,'内容'),(4,'发布时间'),(5,'点赞数')]
    choice_list2 = [(1,'升序'),(2,'降序')]
    type1 = forms.ChoiceField(choices=choice_list1, label='关键字')
    type2 = forms.ChoiceField(choices=choice_list2, label='排序')


class ChoiceFormforSearch(forms.Form):

    choice_list1 = [(1, '默认'),(2,'用户'),(3,'内容'),(4,'发布时间'),(5,'点赞数')]
    choice_list2 = [(1,'升序'),(2,'降序')]
    type1 = forms.ChoiceField(choices=choice_list1, label='关键字')
    type2 = forms.ChoiceField(choices=choice_list2, label='排序')