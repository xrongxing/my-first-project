# -*- coding: utf-8 -*-
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from polls import urls as polls_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 两个url正则同时引用一个app的urls，python manage.py check报警 ?: (urls.W005) URL namespace 'polls' isn't unique. You may not be able to reverse all URLs in this namespace
    #url(r'', include(polls_urls)),
    url(r'^polls/', include('polls.urls')),
]
