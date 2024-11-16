from django.urls import path
from .views import TeacherListView, TeacherDetailView, TeacherCreateView, TeacherUpdateView, TeacherDeleteView

urlpatterns = [
    path('', TeacherListView.as_view(), name='teacher_list'),  # Listar todos os professores
    path('create/', TeacherCreateView.as_view(), name='teacher_create'),  # Criar um novo professor
    path('<int:teacher_id>/', TeacherDetailView.as_view(), name='teacher_detail'),  # Ver detalhes de um professor
    path('<int:teacher_id>/update/', TeacherUpdateView.as_view(), name='teacher_update'),  # Editar professor
    path('<int:teacher_id>/delete/', TeacherDeleteView.as_view(), name='teacher_delete'),  # Excluir professor
]
