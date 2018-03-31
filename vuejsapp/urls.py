# -*- coding: utf-8 -*-

"""
	自定义的路径
	定义vuejs app 的URL模式
"""

from django.conf.urls import url
from django.views.generic.base import TemplateView

from . import views

app_name = 'app_vuejsapp'
urlpatterns = [
    # 
    # url(r'^$', views.index, name='index'), #链接示例API
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'), #添加 vuejsfront/dist/ 中hellovue.html
    url(r'^hellovueapp$', views.hellovueapp, name='hellovueapp' ), 
    url(r'^api$', views.index, name='api_index' ), 
    url(r'^api/add_book$', views.add_book, name='add_book' ), 
    url(r'^api/show_books$', views.show_books, name='show_books' ),
]