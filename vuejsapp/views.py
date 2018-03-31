from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.
from .models import Book

def index(request): #添加示例API
    return HttpResponse("Hello API !") #添加

def hellovueapp(request): 
    msg = 'show demo'
    context = {'show_msg': msg}
    return render(request, 'vuejsapp/hellovueapp.html')

def add_book(request):
    response = {}
    try:
        book = Book(book_name=request.GET.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as err:
        response['msg'] = str(err)
        response['error_num'] = 1

    return JsonResponse(response)

def show_books(request):
    response = {}
    try:
        books = Book.objects.filter()
        response['list']  = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as err:
        response['msg'] = str(err)
        response['error_num'] = 1

    return JsonResponse(response)