from django.urls import path
from . import views

urlpatterns = [
    path('generate-text/', views.generate_text, name='generate_text'),
]
