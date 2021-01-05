from django.urls import path
from . import views
urlpatterns = [
    path('', views.messageview, name='message'),
]