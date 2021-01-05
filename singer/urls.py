from django.urls import path
from . import views
urlpatterns = [
    path('', views.singerView, name='singer'),
    path('.list', views.SingerRankingList.as_view(), name='singerRankingList'),
]