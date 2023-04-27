from django.contrib import admin
from .models import Tests, QuizQuestion, QuizOption, QuizResult


admin.site.register(Tests)
admin.site.register(QuizQuestion)
admin.site.register(QuizOption)
admin.site.register(QuizResult)
