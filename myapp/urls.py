from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Rota para a página inicial
    path('about/', views.about, name='about'),  # Rota para a página "About"
]