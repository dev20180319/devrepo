"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 首页
    url(r'^$', views.index, name='index'),

    # 入门书本中的项目，改为运维日志
    url(r'^learning_logs/', include('learning_logs.urls', namespace='learning_logs')),
    url(r'^users/', include('users.urls', namespace='users')),

    # 预约排队
    url(r'^booklist/', include('booklist.urls', namespace='booklist')),

    # django rest framework 学习，backend restful api
    url(r'^restapi/', include('restapi.urls', namespace='restapi')),
    # api 中的登录
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # echarts
    url(r'^echarts/', include('echarts.urls', namespace='echarts')),

    # 投票 django 1.8 中文文档参考
    url(r'^toupiao/', include('toupiao.urls', namespace='toupiao')),

    # ajax app
    # url(r'^ajax/', include('ajax.urls', namespace='ajax')),

    # weixinapp 微信  werobot
    url(r'^wx/', include('weixinapp.urls', namespace='weixinapp')),

    # vuejsapp 微信  
    url(r'^vuejsapp/', include('vuejsapp.urls', namespace='vuejsapp')),


]
