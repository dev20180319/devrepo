"""
	自定义的路径
	定义learning_logs的URL模式
"""

from django.conf.urls import url

from . import views

app_name = 'app_booklist'
urlpatterns = [
    # 主页-显示菜单
    url(r'^$', views.index, name='index'),

    # 槽车计划
    url(r'^carplans/$', views.carplans, name='carplans'),
    url(r'^pointplans/$', views.pointplans, name='pointplans'),

    # 预约
    url(r'^fanghao/$', views.fanghao, name='fanghao'),
    url(r'^yuehao/$', views.yuehao, name='yuehao'),

    # 排队
    # 输入车牌，查看前后车数量
	url(r'^dengji/$', views.dengji, name='dengji'),
    # 查看排队数量
    url(r'^pointduilie/$', views.pointduilie, name='pointduilie'),
    url(r'^chexuhao/$', views.chexuhao, name='chexuhao'),

	# # 显示某一主题
	# url(r'^book/(?P<topic_id>\d+)/$', views.topic, name='topic'),
	# # 添加新主题
	# url(r'^new_topic/$', views.new_topic ,name='new_topic'),
	# # 添加新条目内容
	# url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
	# # 编辑条目内容
	# url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]

