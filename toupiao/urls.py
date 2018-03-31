"""
	自定义的路径
	定义toupiao的URL模式
"""

from django.conf.urls import url

from . import views

app_name = 'app_toupiao'
urlpatterns = [
    # 主页-投票
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

]

