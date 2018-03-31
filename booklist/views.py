from django.shortcuts import render

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Menu,CarPlan,FangHao,QiangHao,XianChangDuiLie
# from .form import CarPlanForm
# from .models import Entry

from .forms import FangHaoForm,QiangHaoForm


from django.utils.timezone import now, timedelta


#SQL 操作数据库
from django.db import connection

# # 执行自定义sql:
# from django.db import connection
# cursor=connection.cursor()
# #插入操作
# cursor.execute("insert into hello_author(name) values('郭敬明')")
# #更新操作
# cursor.execute('update hello_author set name='abc' where name='bcd'')
# #删除操作
# cursor.execute('delete from hello_author where name='abc'')
# #查询操作
# cursor.execute('select * from hello_author')
# raw=cursor.fetchone() #返回结果行游标直读向前，读取一条
# cursor.fetchall() #读取所有

# #
# Models 操作数据库参考
# http://blog.csdn.net/z5622139/article/details/77683804
#
# models.UserInfo.objects.create(username='andy',password='123456',age=33)
# dic = {"username":"bruce","password":"123456","age":23}
# models.UserInfo.objects.create(**dic)
# ret=UserInfo.objects.all()
# ret=UserInfo.objects.get(id='1')
# ret=UserInfo.objects.filter()
# 条件选取querySet的时候，filter表示=，exclude表示!=。
# querySet.distinct() 去重复
#     __exact 精确等于 like ‘aaa’ __iexact 精确等于 忽略大小写 ilike ‘aaa’
#     __contains 包含 like ‘%aaa%’ __icontains 包含 忽略大小写 ilike ‘%aaa%’，但是对于sqlite来说，contains的作用效果等同于icontains。
#     __gt 大于
#     __gte 大于等于
#     __lt 小于
#     __lte 小于等于
#     __in 存在于一个list范围内
#     __startswith 以…开头
#     __istartswith 以…开头 忽略大小写
#     __endswith 以…结尾
#     __iendswith 以…结尾，忽略大小写
#     __range 在…范围内
#     __year 日期字段的年份
#     __month 日期字段的月份
#     __day 日期字段的日
#     __isnull=True/False
# 如duilie_che = XianChangDuiLie.objects.filter(headerNumber__contains=s_chetou, loadPoint_contains=s_jieshouzhan,
#                                                    zhuangtai=zhuangtai_in)
# models.UserInfo.objects.filter(id=2).delete()
# models.UserInfo.objects.filter(id=1).update(age=18) #找到id=1的数据，将age改为18
# 通过post提交数据：
# models.UserInfo.objects.create(username=request.POST['username'],password=request.POST['password'],age=request.POST['age'])
# return HttpResponse('OK')
#

# Create your views here.


def index(request):
	"""学习笔记的主页"""
	return render(request, 'booklist/index.html')

def carplans(request):
	"""获取车辆计划"""
	postdata=""
	s_chetou = ""
	s_siji = ""
	msg="请查询"

	# 根据输入查找信息
	if request.method == 'POST' :
		postdata=request.POST
		s_chetou=postdata['str_chetou']
		s_siji=postdata['str_siji']
		s_search=s_chetou+s_siji

		if not s_search or not s_search.strip() or len(s_search) < 4 :
			msg = "请输入车牌或司机,搜索长度不小于4。"
			context = {'show_msg': msg, 'str_chetou': s_chetou, 'str_siji': s_siji}
			return render(request, 'booklist/carplans.html', context)

		s_chetou=s_chetou.strip()
		carplans = CarPlan.objects.filter(headNumber__contains=s_chetou,driverName__contains=s_siji).order_by('loadPoint','-sheduleLoadTime')
		if not carplans :
			msg = "没有相关车辆、司机信息"
		else:
			msg = "查询到："
			context = {'carplans': carplans,'show_msg':msg,'str_chetou':s_chetou,'str_siji':s_siji}
			return render(request, 'booklist/carplans.html', context)

	context = {'show_msg': msg,'str_chetou':s_chetou,'str_siji':s_siji}
	return render(request, 'booklist/carplans.html', context)

def pointplans(request):
	"""获取接收站车辆计划"""

	postdata=""
	s_jieshouzhan = ""
	msg="请查询"

	# 根据输入查找信息
	if request.method == 'POST' :
		postdata=request.POST
		s_jieshouzhan=postdata['str_jieshouzhan']

		if not s_jieshouzhan or not s_jieshouzhan.strip() :
			msg = "请输入接收站"
			context = {'show_msg': msg}
			return render(request, 'booklist/pointplans.html', context)

		s_jieshouzhan=s_jieshouzhan.strip()
		carplans = CarPlan.objects.filter(loadPoint__contains=s_jieshouzhan).order_by('loadPoint','-sheduleLoadTime')
		if not carplans :
			msg = "没有相关计划"
		else:
			msg = "查询到："
			context = {'carplans': carplans,'show_msg':msg,'str_jieshouzhan':s_jieshouzhan}
			return render(request, 'booklist/pointplans.html', context)

	context = {'show_msg': msg,'str_jieshouzhan':s_jieshouzhan}
	return render(request, 'booklist/pointplans.html', context)


def fanghao(request):
	"""管理预约号，创建fanghao表,暂未实现角色权限判断"""
	l_fanghao = FangHao.objects.all().order_by("loadPoint", "beginTime")
	context = {}
	context['list_fanghao'] = l_fanghao

	if request.method != 'POST':
		# 未提交数据，创建新表单
		form_fanghao = FangHaoForm()
	else:
		# POST ,提交了数据，对数据进行处理
		form_fanghao = FangHaoForm(data=request.POST)
		if form_fanghao.is_valid():
			new_fanghao = form_fanghao.save(commit=False)
			new_fanghao.save()
			context['show_msg'] = "放号成功"
			return render(request, 'booklist/fanghao.html', context)
			# return HttpResponseRedirect(reverse('booklist:yuehao'))

	context['form_fanghao'] = form_fanghao
	return render(request, 'booklist/fanghao.html', context)



def yuehao(request):
	"""司机约号，根据放号情况选择号段"""
	l_fanghao = FangHao.objects.all().order_by("loadPoint","beginTime")
	context={}
	context['list_fanghao']=l_fanghao

	form_qianghao = QiangHaoForm()

	if request.method == 'POST':
		form_qianghao = QiangHaoForm(data=request.POST)
		if form_qianghao.is_valid():
			form_qianghao = form_qianghao.save(commit=False)
			form_qianghao.isactive = 1
			form_qianghao.save()
			context['show_msg'] = "预约成功"
			form_qianghao = QiangHaoForm()

	context['form_qianghao'] = form_qianghao
	return render(request, 'booklist/yuehao.html', context)

def dengji(request):
	"""登记，输入车牌、状态，自动获取时间、自动查询是否已预约；未来可能获取gps"""
	postdata = ""
	s_chetou = ""
	s_zhuangtai = ""
	date_jintian= now().date() + timedelta(days=0)  # 今天
	date_zuotian = now().date() + timedelta(days=-1)  # 昨天
	date_mingtian = now().date() + timedelta(days=1)  # 明天
	b_dengji=False
	_S_IN,_S_DO,_S_OUT="in","do","out"
	context={}
	context['show_msg']="请查询"

	# 根据输入查找信息
	if request.method == 'POST':
		postdata = request.POST
		s_chetou = postdata.get('str_chetou')
		s_zhuangtai = postdata.get('str_zhuangtai')

		if not s_zhuangtai or not s_zhuangtai.strip() :
			msg = "请选择 “操作” "
			context = {'show_msg': msg, 'str_chetou': s_chetou }
			return render(request, 'booklist/dengji.html', context)

		if not s_chetou or not s_chetou.strip() or len(s_chetou.strip()) < 4:
			msg = "请输入车牌，输入长度不小于4"
			context = {'show_msg': msg, 'str_chetou': s_chetou }
			return render(request, 'booklist/dengji.html', context)
		s_chetou = s_chetou.strip()
		context['str_chetou'] = s_chetou

		# 操作是 “登出”、“作业”、“登入”
		if s_zhuangtai == _S_OUT:
			# in、do 状态的才能登出
			duilie_item=XianChangDuiLie.objects.exclude(zhuangtai=_S_OUT).filter(
				headNumber__contains=s_chetou).order_by("-date_added").first()
			if not duilie_item:
				context['show_msg']="该车未在队列"
				return render(request, 'booklist/dengji.html', context)
			duilie_item.zhuangtai = _S_OUT
			duilie_item.time_out = now()
			duilie_item.save()
			context['show_msg'] = "已登出"
			return render(request, 'booklist/dengji.html', context)

		elif s_zhuangtai == _S_DO:
			# in 状态的才能作业
			duilie_item=XianChangDuiLie.objects.filter(
				headNumber__contains=s_chetou,zhuangtai=_S_IN).order_by("-date_added").first()
			if not duilie_item:
				context['show_msg']="该车未在队列"
				return render(request, 'booklist/dengji.html', context)
			duilie_item.zhuangtai = _S_DO
			duilie_item.time_do = now()
			duilie_item.save()
			context['show_msg'] = "已登记为“正在作业”"
			return render(request, 'booklist/dengji.html', context)

		elif _S_IN == s_zhuangtai:
			# 操作是“登入”
			# 是否已登入
			duilie_item = XianChangDuiLie.objects.filter(
				headNumber__contains=_S_IN).order_by("-date_added").first()
			if duilie_item:
				context['show_msg'] = "该车已登入，不能重复登入"
				return render(request, 'booklist/dengji.html', context)

			# 判断是否在当天计划
			carplan_item = CarPlan.objects.filter(headNumber__contains = s_chetou,
				sheduleLoadTime__range=(date_jintian,date_mingtian)).first()
			if not carplan_item:
				context['show_msg'] = "当天没有该车的计划"
				context['str_chetou']= s_chetou
				return render(request, 'booklist/dengji.html', context)

			# 判断是否有预约
			qianghao_item = QiangHao.objects.filter(idf_carplan=carplan_item.id).first()
			str_qianghao_id=None
			str_youxianji="44_qita"  # 默认优先级为其他
			if qianghao_item:
				context['show_msg'] = "查询到："
				str_qianghao_id=qianghao_item.id


			# 创建队列对象，状态保存为in
			duilie_item=XianChangDuiLie(
				idf_carplan=carplan_item,
				loadPoint = carplan_item.loadPoint,
				headNumber = carplan_item.headNumber,  # 车头车牌
				zhuangtai = _S_IN,  # 状态 in 登入 ；do 操作； out 登出
				youxianji = str_youxianji,
				# 优先级 0_jinji 紧急 ；21_yuyueanshi 预约按时到达 ；22_yuyueweianshi 预约但未按时到达； 33_xianchang 现场，44_qita 其他
				time_in = now(),
				time_do = now(),
				time_out = now(),
				id_s_qianghao =str_qianghao_id
			)
			duilie_item.save()
			context['show_msg'] = "登入完成"
			return render(request, 'booklist/dengji.html', context)

	# 不为post方法
	context['show_msg']="登记车辆状态"
	return render(request, 'booklist/dengji.html', context)

def chexuhao(request):
	"""获取车辆,查看对应队列序号，不能模糊查询"""

	postdata=""
	s_chetou = ""
	__ZHUANGTAI="in"    # 其他状态有do 、out
	msg="请查询"
	l_duilie = ""
	l_size=""

	# 根据输入查找信息
	if request.method == 'POST' :
		postdata=request.POST
		s_chetou = postdata['str_chetou']

		if not s_chetou or not s_chetou.strip() or len(s_chetou) < 4:
			msg = "请输入车牌，输入长度不小于4"
			context = {'show_msg': msg, 'str_chetou': s_chetou}
			return render(request, 'booklist/chexuhao.html', context)

		s_chetou=s_chetou.strip()
		# 根据车牌，查询所在接收站
		car_item=XianChangDuiLie.objects.filter(
			headNumber__contains=s_chetou,zhuangtai=__ZHUANGTAI).first()

		if not car_item :
			msg = "车辆没在队列"
			context = {'show_msg': msg}
			return render(request, 'booklist/chexuhao.html', context)
		else:
			s_jieshouzhan=car_item.loadPoint

			l_duilie = XianChangDuiLie.objects.filter(
			loadPoint__contains=s_jieshouzhan,zhuangtai=__ZHUANGTAI).order_by('youxianji','time_in')

		_temp_num=0
		for _temp_item in l_duilie:
			if(_temp_item.headNumber == car_item.headNumber):
				break
			else:
				_temp_num = _temp_num+1

		n_listsize = len(l_duilie)
		n_carindex=_temp_num
		msg = "查询到："
		context = {'show_msg':msg,'str_chetou':s_chetou,"car_item":car_item,'num_carindex':n_carindex ,"num_listsize":n_listsize}
		return render(request, 'booklist/chexuhao.html', context)

	context = {'show_msg': msg,'str_chetou':s_chetou}
	return render(request, 'booklist/chexuhao.html', context)


def pointduilie(request):
	"""获取接收站车辆排队情况"""

	postdata=""
	s_jieshouzhan = ""
	_S_IN="in"    # 其他状态有do 、out
	_S_DO = "do"
	msg="请查询"
	l_jieshouzhan = ""
	l_size=""

	# 根据输入查找信息
	if request.method == 'POST' :
		postdata=request.POST
		s_jieshouzhan=postdata['str_jieshouzhan']

		if not s_jieshouzhan or not s_jieshouzhan.strip() :
			msg = "请输入接收站"
			context = {'show_msg': msg}
			return render(request, 'booklist/pointduilie.html', context)

		s_jieshouzhan=s_jieshouzhan.strip()
		duilie_in = XianChangDuiLie.objects.filter(
			loadPoint__contains=s_jieshouzhan,zhuangtai=_S_IN).order_by('youxianji','time_in')
		duilie_do = XianChangDuiLie.objects.filter(
			loadPoint__contains=s_jieshouzhan, zhuangtai=_S_DO).order_by('time_do')

		if duilie_in or duilie_do:
			msg = "查询到："
			in_size = len(duilie_in)
			do_size = len(duilie_do)
			context = {'show_msg':msg,'str_jieshouzhan':s_jieshouzhan ,'duilie_in': duilie_in,"in_size":in_size}
			context['do_size']=do_size
			context['duilie_do'] = duilie_do
			return render(request, 'booklist/pointduilie.html', context)
		else:
			msg = "队列中没有车辆"
		

	context = {'show_msg': msg,'str_jieshouzhan':s_jieshouzhan}
	return render(request, 'booklist/pointduilie.html', context)
