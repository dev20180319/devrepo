from django.contrib import admin
from .models import Menu,CarPlan,FangHao,QiangHao,XianChangDuiLie


# Register your models here.
# 注册自己的模型

admin.site.register(Menu)
admin.site.register(FangHao)
admin.site.register(QiangHao)
admin.site.register(CarPlan)
admin.site.register(XianChangDuiLie)
