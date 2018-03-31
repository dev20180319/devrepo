"""
	自定义的路径
	定义learning_logs的URL模式
"""

from django.conf.urls import url

from . import views

app_name = 'app_learning_logs'
urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),

    # 显示所有的主题
    url(r'^topics/$', views.topics, name='topics'),
	# 显示某一主题
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
	# 添加新主题
	url(r'^new_topic/$', views.new_topic ,name='new_topic'),
	# 添加新条目内容
	url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
	# 编辑条目内容
	url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]

