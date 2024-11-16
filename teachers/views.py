from django.http import JsonResponse
from django.views import View
from .models import Teacher
from django.shortcuts import get_object_or_404, render, redirect
from .forms import TeacherForm


class TeacherListView(View):
    def get(self, request):
        teachers = list(Teacher.objects.all().values(
            'id', 'first_name', 'last_name', 'email', 'hire_date'
        ))
        return JsonResponse(teachers, safe=False)
    
class TeacherDetailView(View):
    def get(self, request, teacher_id):
        teacher = get_object_or_404(Teacher, id=teacher_id)
        data = {
            'id': teacher.id,
            'first_name': teacher.first_name,
            'last_name': teacher.last_name,
            'email': teacher.email,
            'phone_number': teacher.phone_number,
            'hire_date': teacher.hire_date,
            'subjects': list(teacher.subjects.values_list('name', flat=True))  # Listando as disciplinas
        }
        return JsonResponse(data)
    
class TeacherCreateView(View):
    def get(self, request):
        form = TeacherForm()  # Criando uma instância vazia do formulário
        return render(request, 'teachers/teacher_form.html', {'form': form})

    def post(self, request):
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')  # Redireciona para a lista de professores
        return render(request, 'teachers/teacher_form.html', {'form': form})

class TeacherUpdateView(View):
    def get(self, request, teacher_id):
        teacher = get_object_or_404(Teacher, id=teacher_id)
        form = TeacherForm(instance=teacher)  # Preenche o formulário com os dados existentes
        return render(request, 'teachers/teacher_form.html', {'form': form})

    def post(self, request, teacher_id):
        teacher = get_object_or_404(Teacher, id=teacher_id)
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_detail', teacher_id=teacher.id)  # Redireciona para a página de detalhes
        return render(request, 'teachers/teacher_form.html', {'form': form})

class TeacherDeleteView(View):
    def post(self, request, teacher_id):
        teacher = get_object_or_404(Teacher, id=teacher_id)
        teacher.delete() 
        return JsonResponse({'message': 'Professor excluído com sucesso'}, status=204)
