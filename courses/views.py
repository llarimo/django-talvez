from django.http import JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404
from .models import Courses
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from .models import Courses
from .forms import CourseForm


def course_list(request):
    # Buscar todos os cursos
    courses = Courses.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, course_id):
    # Buscar o curso específico pelo ID
    course = get_object_or_404(Courses, id=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})



def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')  # Redireciona para a lista de cursos após a criação
    else:
        form = CourseForm()

    return render(request, 'courses/create_course.html', {'form': form})