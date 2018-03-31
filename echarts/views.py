# echarts/views.py
from django.shortcuts import render

# Create your views here.
# 
def index(request):
	"""echarts主页"""
	return render(request, 'echarts/index.html')