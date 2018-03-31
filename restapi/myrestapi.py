from rest_framework import serializers
from rest_framework import viewsets

from django.contrib.auth.models import User, Group
from .models import Blog
from booklist.models import CarPlan,FangHao,QiangHao,XianChangDuiLie



# ##############   Serializer序列化models   #############
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups',)

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name',)

class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        depth = 1
        # fields = ('url','title','content',)
        fields = '__all__'

class CarPlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarPlan
        # fields = ('url','headNumber','sheduleLoadTime','loadPoint','driverName',)
        fields = '__all__'

class FangHaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FangHao
        fields = ('url','nameYuYueHao','sheduleLoadTime','loadPoint','beginTime','endTime','numHao',)
class QiangHaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QiangHao
        fields = ('url','idf_carplan','idf_fanghao','isactive',)
class XianChangDuiLieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = XianChangDuiLie
        fields = ('url','idf_carplan','loadPoint','headNumber','zhuangtai','youxianji','time_in','time_do','time_out','idf_qianghao')

# ##############   view set   #############
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class CarPlanViewSet(viewsets.ModelViewSet):
    queryset = CarPlan.objects.all()
    serializer_class = CarPlanSerializer


class FangHaoViewSet(viewsets.ModelViewSet):
    queryset = FangHao.objects.all()
    serializer_class = FangHaoSerializer


class QiangHaoViewSet(viewsets.ModelViewSet):
    queryset = QiangHao.objects.all()
    serializer_class = QiangHaoSerializer


class XianChangDuiLieViewSet(viewsets.ModelViewSet):
    queryset = XianChangDuiLie.objects.all()
    serializer_class = XianChangDuiLieSerializer
