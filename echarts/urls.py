"""
	自定义的路径
	定义echarts的URL模式
"""

from django.conf.urls import url

from . import views

app_name = 'app_echarts'
urlpatterns = [
    # 主页-显示菜单
    url(r'^$', views.index, name='index'),

    
]

