from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.example_view, name="example_view"),
    # path('api/upload-notes/', views.upload_notes, name="upload_notes"),
    path('api/get_questions/', views.get_questions, name="get_questions"),
]