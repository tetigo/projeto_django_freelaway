from django.urls import path
from . import views

urlpatterns = [
    path('encontrar_jobs/', views.encontrar_jobs, name='encontrar_jobs_url'),
    path('aceitar_job/<int:id>/', views.aceitar_job, name='aceitar_job_url'),
    path('perfil/', views.perfil, name='perfil_url'),
    path('enviar_projeto/', views.enviar_projeto, name='enviar_projeto_url'),
    
]
