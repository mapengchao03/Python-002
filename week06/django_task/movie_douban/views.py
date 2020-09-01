from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from .import models


# Create your views here.


#主显示页面
def index(request):
    return HttpResponseRedirect("/admin/")
    # return HttpResponse("hello world")


# int
def int_url(request, year):
    return HttpResponse(year)


# str
def name_url(request, **kwargs):
    return HttpResponse(str(kwargs['year']) + kwargs['name'])


# myyear
def myyear(request, year):
    return render(request, 'myyear.html', {'year': year})


# 搜索以及默认显示星级大于3
def search_result(request):

    if request.method == 'POST':
        return JsonResponse({"result": False, "error_code": 20000, "method": "failed"})
    else:

        star_number = request.GET.get('star', '')
        short_comment = request.GET.get('short_comment', '')
        if star_number and short_comment:
            condition = f'星级等于"{star_number}",短评包含"{short_comment}"'
            data = models.MovieShortComments.objects.filter(star=star_number, short_comment__contains=short_comment).values()
        elif star_number and short_comment == '':
            condition = f'星级等于"{star_number}"'
            data = models.MovieShortComments.objects.filter(star=star_number).values()
        elif star_number == '' and short_comment:
            condition = f'短评包含"{short_comment}"'
            data = models.MovieShortComments.objects.filter(short_comment__contains=short_comment).values()
        else:
            condition = f'默认星级大于"3""'
            data = models.MovieShortComments.objects.filter(star__gt=3).values()
        return render(request, 'index.html', {'data': data, 'condition': condition})
