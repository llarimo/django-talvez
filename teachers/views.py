from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django import forms
from .models import Teacher
from django.http import JsonResponse

# Definição do formulário diretamente na view
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'subject', 'hire_date']

def teacher_list(request):
    teachers = Teacher.objects.all()
    return JsonResponse(request, 'teachers/teacher_list.html', {'teachers': teachers})

def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return JsonResponse(request, 'teachers/teacher_detail.html', {'teacher': teacher})

def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'teachers/teacher_form.html', {'form': form})

def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_detail', pk=teacher.pk)
    else:
        form = TeacherForm(instance=teacher)
    return JsonResponse(request, 'teachers/teacher_form.html', {'form': form})

def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
    return JsonResponse(request, 'teachers/teacher_confirm_delete.html', {'teacher': teacher})
