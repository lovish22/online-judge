from django.contrib import admin

from .models import Problem, Solution, TestCases, User

admin.site.register(Problem)
admin.site.register(Solution)
admin.site.register(TestCases)
admin.site.register(User)
# Register your models here.
