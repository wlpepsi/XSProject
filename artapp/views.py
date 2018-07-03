from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # print(request.META.keys())
    print(request.GET)

    return render(request, 'art/index.html',context={'name':'宝强','age':32},status=302)
    # return HttpResponse('<h1>nihao</h1>')
    # return JsonResponse({'status':302,'message':'重定向'})