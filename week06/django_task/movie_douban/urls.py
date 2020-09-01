from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:year>', views.int_url, name='int_url'),
    path('<int:year>/<str:name>', views.name_url, name='name_url'),
    # re_path('(?P<year>[0-9]{4}).html', views.myyear, name='myyear'),
    re_path('(?P<year>[0-9]{4}).html', views.myyear, name='myyear'),
    # 显示星级大于3短评和搜索框
    path('short_comments', views.search_result),
]
