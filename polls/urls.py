from django.conf.urls import url
from . import views as polls_views

urlpatterns = [
    url(r'^$', polls_views.index, name='index'),
]
