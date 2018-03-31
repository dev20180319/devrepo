#-*-coding:UTF-8-*-

from django.db import models


# 模型
class Menu(models.Model):
	"""微信号、所属角色、操作url"""
	# topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	weixinhao = models.CharField(max_length = 200)
	juese = models.CharField(max_length = 200)
	urlcaozuo = models.TextField()
	text_beizhu = models.TextField(blank=True,null=True)
	# date_plan = models.DateTimeField(auto_now_add=True)
	# owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		"""返回模型的字符串表示"""
		if len(self.text_beizhu) < 50:
			return self.text_beizhu
		else:
			return	self.text_beizhu[:50] + '...'

class CarPlan(models.Model):
	"""从槽车系统同步的计划"""

	"""接口数据格式：
	{"total":"1","message":"",
		"data":[
			{"HeadNumber":"冀R71558","ScheduleLoadTime":"2018-03-02 08:00:00",
			"LoadPoint":"浙江宁波LNG槽车站","DriverName":"韩东","ConvoyName":"胡拥军"}
		],"success":"true"}
	"""
	
	headNumber = models.CharField(max_length = 200)
	sheduleLoadTime = models.DateTimeField()
	loadPoint = models.CharField(max_length = 200)
	driverName = models.CharField(max_length = 200)
	convoyName = models.CharField(max_length = 200,blank=True,null=True)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""返回模型的字符串表示"""
		return "槽车计划："+"司机，"+self.driverName +"； 接收站，"\
			   + self.loadPoint  +"； 时间，"+ str(self.sheduleLoadTime) +"；"

class FangHao(models.Model):
	"""预约号"""
	nameYuYueHao=models.CharField(max_length=200,blank=True,null=True)
	sheduleLoadTime = models.DateTimeField()
	loadPoint = models.CharField(max_length=200)
	beginTime = models.DateTimeField()
	endTime=models.DateTimeField()
	numHao=models.IntegerField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		"""返回模型的字符串表示"""
		return "放号："+"接收站，"+ self.loadPoint  +"； 时间，"+ str(self.sheduleLoadTime)+ self.nameYuYueHao +" 放号"+ str(self.numHao) +"个"

class QiangHao(models.Model):
	idf_carplan=models.ForeignKey(CarPlan, on_delete=models.CASCADE)
	idf_fanghao = models.ForeignKey(FangHao, on_delete=models.CASCADE)
	weixinhao=models.CharField(max_length=200)
	isactive = models.IntegerField()    # 激活1
	date_added = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		"""返回模型的字符串表示"""
		return "已预约："+"计划，"+ str(self.idf_carplan) +"； 预约阶段，"+ str(self.idf_fanghao)+ "; 状态"+ str(self.isactive)

class XianChangDuiLie(models.Model):
	idf_carplan=models.ForeignKey(CarPlan, on_delete=models.CASCADE)
	loadPoint = models.CharField(max_length=200)	#接收站
	headNumber = models.CharField(max_length=200)	#车头车牌
	zhuangtai = models.CharField(max_length=20)		#状态 in 登入 ；do 操作； out 登出
	youxianji = models.CharField(max_length=20)
	#优先级 0_jinji 紧急 ；21_yuyueanshi 预约按时到达 ；22_yuyueweianshi 预约但未按时到达； 33_xianchang 现场，44_qita 其他
	time_in = models.DateTimeField(blank=True,null=True)
	time_do = models.DateTimeField(blank=True,null=True)
	time_out = models.DateTimeField(blank=True,null=True)
	date_added = models.DateTimeField(auto_now_add=True)
	idf_qianghao = models.ForeignKey(QiangHao,on_delete=models.CASCADE,max_length=20,blank=True,null=True)
	def __str__(self):
		"""返回模型的字符串表示"""
		return "队列："+"接收站，"+ str(self.loadPoint) +"； 车，"+ str(self.headNumber)+ "; 状态为"+ str(self.zhuangtai)
