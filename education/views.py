from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Lesson
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.core import serializers
import json

@login_required(login_url='/login/')
def index(request):
    return render(request, 'courses.html', locals())

@login_required(login_url='/login/')
def get_courses(request):
    myCourses = Lesson.objects.order_by('-start_date')
    allCourses = Lesson.objects.order_by('-start_date')
    myCourses = serializers.serialize('json', myCourses)
    allCourses = serializers.serialize('json', allCourses)

    data = {
            'myCourses': myCourses,
            'allCourses': allCourses
        }
    return HttpResponse(json.dumps(data), content_type="application/json")