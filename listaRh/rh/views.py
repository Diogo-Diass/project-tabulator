from django.shortcuts import render
from django.views.generic import TemplateView
import json
from datetime import date, datetime
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.paginator import Paginator
from rh import models
from django.db.models import Q

class CriarFuncionarios(TemplateView):
    template_name = 'form_funcionario.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teste"] = 'teste'
        return context
    
    def post(self, request, *args, **kwargs):
        
        funcionario = models.Funcionario()
        funcionario.data_admissao = request.POST['data_admissao']
        funcionario.nascimento = request.POST['nascimento']
        funcionario.nome = request.POST['nome']
        funcionario.cargo = request.POST['cargo']
        funcionario.tipo_cargo = request.POST['tipo_cargo']
        funcionario.data_saida = request.POST['data_saida'] if request.POST['data_saida'] else None
        funcionario.codigo_funcional = request.POST['codigo_funcional']
        
        funcionario.save()
        
        return HttpResponse('Dados recebidos via POST')
    
    
class ListaFuncionarios(TemplateView):
    template_name = 'lista_dados.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teste"] = 'teste'
        
        funcionarios = models.Funcionario.objects.all()
        
        dados_funcionarios = []
        
        for func in funcionarios:
 
            json_func = {}
            
            for field in models.Funcionario._meta.fields:
              
                campo_nome = field.name
                
                campo_valor = getattr(func, campo_nome)
                
                if campo_nome in ['nascimento', 'data_admissao', 'data_saida'] and isinstance(campo_valor, (date, datetime)):
                 
                    json_func[campo_nome] = campo_valor.isoformat()
                
                else:
                    json_func[campo_nome] = campo_valor

            dados_funcionarios.append(json_func)
    
        context['dados_funcionarios'] = json.dumps(dados_funcionarios)
        
        return context
    

from django.core.paginator import Paginator
from django.http import JsonResponse
from . import models

def lista_funcionarios_ajax(request):
    page_size = int(request.GET.get('pageSize', 10))
    page_number = int(request.GET.get('page', 1))

    # Pega o valor do filtro de pesquisa (se houver)
    pesquisa_nome = request.GET.get('headerFilter_nome', None)
    
    # Filtra os funcionários com base na pesquisa (se houver)
    if pesquisa_nome:
        funcionarios = models.Funcionario.objects.filter(nome__icontains=pesquisa_nome)
    else:
        funcionarios = models.Funcionario.objects.all()

    # Pagina os resultados
    paginator = Paginator(funcionarios, page_size)
    page = paginator.get_page(page_number)

    dados_funcionarios = [
        {
            "nome": func.nome,
            "cargo": func.cargo,
            "data_nascimento": func.nascimento.isoformat() if func.nascimento else None,
        }
        for func in page.object_list
    ]

    resposta = {
        'data': dados_funcionarios,
        'last_page': paginator.num_pages, 
        'last_row': paginator.count
    }

    return JsonResponse(resposta)