# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views as polls_views

# url names 的命名空间
app_name = 'polls'

urlpatterns = [
    #url(r'^$', polls_views.index, name='index'),
    #url(r'^(?P<question_id>[0-9]+)/$', polls_views.detail, name='detail'),
    #url(r'^(?P<question_id>[0-9]+)/results/$', polls_views.results, name='results'),
    #url(r'^(?P<question_id>[0-9]+)/vote/$', polls_views.vote, name='vote'),

    url(r'^$', polls_views.IndexView.as_view(), name='index'),
    # DetailView类视图需要从url捕获到的称为"pk"的主键值，因此我们在url文件中将2和3条目的<question_id>修改成了<pk>
    url(r'^(?P<pk>[0-9]+)/$', polls_views.DetailView.as_view(), name='detail'),
    # DetailView类视图需要从url捕获到的称为"pk"的主键值，因此我们在url文件中将2和3条目的<question_id>修改成了<pk>
    url(r'^(?P<pk>[0-9]+)/results/$', polls_views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', polls_views.vote, name='vote'),
]
