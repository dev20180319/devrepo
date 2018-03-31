"""
	自定义的路径
	定义restapi 的URL模式
"""

from django.conf.urls import include, url

# rest 引用
from rest_framework import routers
from . import myrestapi

# 注册各类viewset
router = routers.DefaultRouter()
router.register(r'users', myrestapi.UserViewSet)
router.register(r'groups', myrestapi.GroupViewSet)
router.register(r'blogs', myrestapi.BlogViewSet)
router.register(r'carplan', myrestapi.CarPlanViewSet)
router.register(r'fanghao', myrestapi.FangHaoViewSet)
router.register(r'qianghao', myrestapi.QiangHaoViewSet)
router.register(r'xianchangduilie', myrestapi.XianChangDuiLieViewSet)


app_name = 'app_restapi'
urlpatterns = [
    # 将注册的viewset 的url 对应
    url(r'^', include(router.urls)),


]

