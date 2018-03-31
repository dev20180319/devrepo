from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic
from .models import Entry
from .forms import TopicForm, EntryForm


# Create your views here.

def index(request):
	"""学习笔记的主页"""
	return render(request, 'learning_logs/index.html')

# 所有人均能看到项目
# @login_required
def topics(request):
	"""显示所有的项目"""
	topics = Topic.objects.order_by('date_added')
	
	# 显示用户所属的主题
	# topics = Topic.objects.filter(owner=request.user).order_by('date_added')
	context = {'topics':topics}
	return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
	"""显示某一特定tipic,用entries"""
	topic = get_object_or_404(Topic, id=topic_id)
	
	# 只能看到自己创建的内容
	entries = topic.entry_set.filter(owner=request.user).order_by('-date_added')
	context = {'topic':topic, 'entries': entries}
	return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
	"""添加新主题"""
	if request.method != 'POST':
		# 未提交数据，创建新表单
		form = TopicForm()
	else:
		# POST ,提交了数据，对数据进行处理
		form = TopicForm(data=request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			# new_topic.owner = request.user
			new_topic.save()
			return HttpResponseRedirect(reverse('learning_logs:topics'))

	context = {'form': form}
	return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
	"""添加某tpoic_id主题的新内容"""
	topic = get_object_or_404(Topic, id=topic_id)

	# 项目所有者才能新建内容
	# if topic.owner != request.user:
	# 	raise Http404

	if request.method != 'POST':
		form=EntryForm()
	else:
		form=EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic_id = topic_id
			new_entry.owner = request.user
			new_entry.save()
			return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))

	context = {'topic':topic, 'form':form}
	return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
	"""编辑某一条目内容"""
	entry = get_object_or_404(Entry, id=entry_id)
	topic = entry.topic

	# 创建者才能编辑内容
	if entry.owner != request.user:
		raise Http404

	if request.method != 'POST':
		form = EntryForm(instance = entry)
	else:
		form = EntryForm(instance = entry , data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
	context = {'entry':entry, 'topic':topic, 'form':form}
	return render(request, 'learning_logs/edit_entry.html', context)




