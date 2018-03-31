"""
	自定义的路径
	定义 users 的URL模式
"""

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

app_name = 'app_users'

urlpatterns = [
    # 登录页面
    url(r'^$', login, {'template_name': 'users/login.html'}, 
    	name='login'),
    url(r'^login/$', login, {'template_name': 'users/login.html'}, 
    	name='login'),
	url(r'^logout/$', views.logout_view, name='logout'),
	url(r'^register/$', views.register, name='register'),

]

