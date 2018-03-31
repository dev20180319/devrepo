from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    # 这里利用了django自身的登陆验证系统
    # if not request.user.is_authenticated():
    #     return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/admin/'))

    a = {}
    a["result"] = "post_success"
    return HttpResponse(json.dumps(a), content_type='application/json')