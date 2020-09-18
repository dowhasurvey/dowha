from django.contrib import admin
#관리자 페이지에 Question 등록
from .models import Question
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']
admin.site.register(Question,QuestionAdmin)
#관리자 페이지 Answer 등록
from .models import Answer
class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['subject']
admin.site.register(Answer, AnswerAdmin)