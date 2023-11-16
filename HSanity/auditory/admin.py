from django.contrib import admin
from .models import *

# Register your models here.

class AnswerInLine(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInLine]

admin.site.register(Audit)
admin.site.register(Section)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(AuditResult)
admin.site.register(SectionResult)
admin.site.register(AuditFile)


