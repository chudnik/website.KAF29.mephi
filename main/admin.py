from django.contrib import admin
from .models import Courses, News, Teachers


# Register your models here.
@admin.register(Courses)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass


@admin.register(Teachers)
class TeacherAdmin(admin.ModelAdmin):
    pass
