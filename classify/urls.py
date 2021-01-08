from django.urls import path
from . import views
urlpatterns = [
    path('', views.classifyView, name='classify'),
    # path('<str:song_type>', views.classifyView, name='classify1'),
]