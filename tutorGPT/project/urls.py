from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.example_view, name="competitionSettingsFormView"),
]