from django.shortcuts import render
from .models import Lesson, Pupil, Teacher
# Create your views here.
from django.http import HttpResponse


def index(request):
    teachers = Teacher.objects.all()
    return render(request, 'main/index.html', {'teachers': teachers, 'list': 'Учителя'} )


def profile(request, teacher_name='Альбус'):
    teacher = Teacher.objects.filter(firstName=teacher_name)
    pupils = teacher[0].pupil_set.all()
    return render(request, 'main/profile.html', {'teacher': teacher[0], 'pupils': pupils, 'list': 'Ученики'} )
