from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def logout_view(request):
	"""注销用户"""
	logout(request)
	return HttpResponseRedirect(reverse('users:login'))

def register(request):
	"""注册用户"""
	if request.method != 'POST':
		# 显示空注册表
		form = UserCreationForm()
	else:
		# Post，已填写完毕提交 
		form = UserCreationForm(data = request.POST)

		if form.is_valid():
			new_user = form.save()
			# 注册成功，自动登录
			authenticated_user=authenticate(username=new_user.username,
				password=request.POST['password1'])
			print(request.POST['password1'])
			login(request, authenticated_user)
			return HttpResponseRedirect(reverse('learning_logs:index'))

	context = {'form': form}
	return render(request, 'users/register.html', context)


