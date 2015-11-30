from django.contrib import admin
from polls.models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        ('Qeustion Statement', {'fields': ['question_text']}),
        ('Date Statement', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

# Register your models here.
