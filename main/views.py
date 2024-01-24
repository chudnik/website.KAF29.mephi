from django.shortcuts import render

# Create your views here.

from main.models import Courses, Teachers, News

def index_page(request):
    context = {}
    context['news'] = News.objects.all()
    return render(request, 'index.html', context)

def lesson_page(request):
    context = {}
    context['courses'] = Courses.objects.all()
    return render(request, 'lesson.html', context)

def teachers_page(request):
    context = {}
    context['teachers'] = Teachers.objects.all()
    return render(request, 'teachers.html', context)
