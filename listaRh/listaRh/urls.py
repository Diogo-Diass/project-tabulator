
from django.contrib import admin
from django.urls import path
from rh import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('funcionarios/', views.CriarFuncionarios.as_view(), name='criar_func'),
    path('lista_dados/', views.ListaFuncionarios.as_view(), name='lista_dados'),
    path('funcionarios/ajax/', views.lista_funcionarios_ajax, name='sua_view_ajax'),
]
