# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Question, Choice
from django.shortcuts import get_object_or_404

# Register your models here.

#class ChoiceInline(admin.StackedInline):
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'votes',)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently',)
    list_filter = ['pub_date',]
    search_fields = ['question_text',]
    #fields = ['pub_date', 'question_text',]

    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    # ChoiceInline class 要放在QuestionAdmin上面
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
