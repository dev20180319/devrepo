from django import forms

from .models import CarPlan,FangHao,QiangHao

# 处理表单

class CarPlanForm(forms.ModelForm):
	"""提交CarPlan表单"""
	class Meta:
		model = CarPlan
		fields = "__all__"


class FangHaoForm(forms.ModelForm):
    """提交CarPlan表单"""
    class Meta:
        model = FangHao
        fields = "__all__"
        label={}
        label['sheduleLoadTime'] = '计划日期'
        label['nameYuYueHao'] = '预约阶段'
        label['loadPoint'] = 'LNG接收站'
        label['beginTime'] = '开始时间'
        label['endTime'] = '结束时间'
        label['numHao'] = '放号数量'

class QiangHaoForm(forms.ModelForm):
    """提交qianghao表单"""
    class Meta:
        model = QiangHao
        fields = "__all__"

# class EntryForm(forms.ModelForm):	
# 	"""提交Entry"""
# 	class Meta:
# 		model = Entry
# 		fields = {'text'}
# 		label = {'text':''}
# 		widgets = {'text': forms.Textarea(attrs={'cols':80})}



""" 写frorms参考
	# username = models.CharField(max_length=32)    <-- models
    username = fields.CharField(max_length=32)
    # email = models.EmailField()    <-- models
    email = fields.EmailField()
    # user_type = models.ForeignKey(to='UserType',to_field='id')    <-- models
    user_type = fields.ChoiceField(
        choices=models.UserType.objects.values_list('id','caption')
    )

    # 下面的操作是让数据在网页上实时更新。
    def __init__(self, *args, **kwargs):
        super(UserInfoForm,self).__init__(*args, **kwargs)
        self.fields['user_type'].choices = models.UserType.objects.values_list('id','caption')


	model = models.UserInfo    # 与models建立了依赖关系
	fields = "__all__"
"""
		
						
