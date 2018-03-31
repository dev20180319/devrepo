from django import forms

from .models import Topic, Entry

# 处理表单

class TopicForm(forms.ModelForm):
	"""提交Topic表单"""
	class Meta:
		model = Topic
		fields = {'text'}
		label = {'text': ''}

class EntryForm(forms.ModelForm):	
	"""提交Entry"""
	class Meta:
		model = Entry
		fields = {'text'}
		label = {'text':''}
		widgets = {'text': forms.Textarea(attrs={'cols':80})}


		
						
