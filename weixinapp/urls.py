"""
	自定义的路径
	定义echarts的URL模式
"""

from django.conf.urls import url

from werobot.contrib.django import make_view
from . import weixinrobot
from . import views

app_name = 'app_weixinapp'
urlpatterns = [
    # 主页-显示菜单
    url(r'^robot/', make_view(weixinrobot.myrobot), name='robot'),

    url(r'^getsignconfig$', views.getsignconfig, name='getsignconfig'),

    url(r'^demo$', views.demo, name='demo'),

]

