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


# short_comments start > 3
def short_comments(request):

    data = models.MovieShortComments.objects.filter(star__gt=3).values()
    return render(request, 'index.html', {'data': data})


# 搜索
# def search_result(request):
#
#     if request.method == 'POST':
#         return JsonResponse({"result": False, "error_code": 20000, "method": "failed"})
#     else:
#         if '4' in request.Get.get('star'):
#             return JsonResponse({"result": False, "error_code": 20000, "method": request.url})
#         if star_number is not None and text is not None:
#             data = models.MovieShortComments.objects.filter(star=star_number, short_comment__contains=text).values()
#         elif star_number is not None and text is None:
#             data = models.MovieShortComments.objects.filter(star=star_number).values()
#         elif star_number is None and text is not None:
#             data = models.MovieShortComments.objects.filter(short_comment__contains=text).values()
#         else:
#             data = models.MovieShortComments.objects.filter(star__gt=3).values()
#         return render(request, 'search.html', {'data': data})
