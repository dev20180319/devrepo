"""
	自定义的路径
	定义ajax的URL模式
"""

from django.conf.urls import url

from . import views

app_name = 'app_ajax'
urlpatterns = [
    # 主页-ajax
    url(r'^$', views.index(), name='index'),


]

