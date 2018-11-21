# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.views import generic
from .models import Question, Choice

# Create your views here.

#def index(request):
#    #return HttpResponse("Hello")
#    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    #output = ',<br /> '.join([q.question_text for q in latest_question_list])
#    #return HttpResponse(output)
#
#    #template = loader.get_template('polls/index.html')
#    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    #context = {
#    #    'latest_question_list': latest_question_list,
#    #}
#    #return HttpResponse(template.render(context, request))
#    
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    context = {
#        'latest_question_list': latest_question_list,
#    }
#    return render(request, 'polls/index.html', context)
#
#def detail(request, question_id):
#    #return HttpResponse("You are looking detail question %s." % question_id)
#
#    #try:
#    #    question = Question.objects.get(pk=question_id)
#    #except Question.DoesNotExist:
#    #    raise Http404("Question does not exist.")
#    #context = {
#    #    'question': question,
#    #}
#    #return render(request, 'polls/detail.html', context)
#
#    question = get_object_or_404(Question, pk=question_id)
#    context = {
#        'question': question,
#    }
#    return render(request, 'polls/detail.html', context)
#
#def results(request, question_id):
#    #results = "You are looking results question %s."
#    #return HttpResponse(results % question_id)
#    question = get_object_or_404(Question, pk=question_id)
#    context = {
#        'question': question,
#    }
#    return render(request, 'polls/results.html', context)


class IndexView(generic.ListView):
    # ListView类视图使用一个默认模板称为<app name>/<model name>_list.html
    template_name = 'polls/index.html'
    # 对于ListView，自动生成的上下文变量是question_list。为了覆盖它，我们提供了context_object_name属性，指定说我们希望使用latest_question_list而不是question_list
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    # DetailView类视图使用一个称作<app name>/<model name>_detail.html的模板
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    # DetailView类视图使用一个称作<app name>/<model name>_detail.html的模板
    template_name = 'polls/results.html'

def vote(request, question_id):
    #return HttpResponse("You are looking vote question %s." % question_id)

    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 发生choice未找到异常时，重新返回表单页面，给出提示信息
        context = {
            'question': question,
            'error_message': "You didn't select a choice.",
        }
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # 成功处理数据后，自动跳转到结果页面，防止用户连续多次提交
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
