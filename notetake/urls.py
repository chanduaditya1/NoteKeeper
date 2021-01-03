from django.urls import path
from . import views

urlpatterns = [
	path('dashboard/',views.note_list, name="note_list"),
	path('note/<int:pk>/', views.note_detail, name='note_detail'),
	path('note/new/', views.note_new, name='note_new'),
	path('note/<int:pk>/edit', views.note_edit, name='note_edit'),
	path('note/<pk>/delete', views.note_delete, name='note_delete'),
	path('register', views.register, name='register'),
]