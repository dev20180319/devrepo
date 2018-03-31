from django.shortcuts import render

from django.http import JsonResponse
from django.http import HttpResponse

from . import weixinrobot

# Create your views here.


def getsignconfig(request):
    surl=""
    if request.method == 'GET' and 'strurl' in request.GET:
            surl = request.GET.get('strurl')
    if request.method == 'POST' and 'strurl' in request.POST:
            surl = request.POST.get('strurl')
    if not surl:
        return HttpResponse('提供 strurl 参数')
        
    return JsonResponse(weixinrobot.get_sign_config(surl))

def demo(request):
    msg = 'show demo'
    _s_full_url = request.scheme + "://" + request.get_host() + request.get_full_path()
    context = {'show_msg': msg, 'full_url': _s_full_url , 'sign_config': weixinrobot.get_sign_config(_s_full_url) }
    return render(request, 'weixinapp/demo.html', context)