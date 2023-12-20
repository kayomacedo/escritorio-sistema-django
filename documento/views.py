from django.http import HttpResponse
from django.shortcuts import redirect, render
from documento.models import Pessoa,Documento


def novo_documento(request):
    pessoas = Pessoa.objects.all()

    if request.method == 'POST':
        # Obtenha os dados do formulário
        titulo = request.POST.get('titulo')
        resumo = request.POST.get('resumo')
        pessoas_envolvidas_ids = request.POST.getlist('pessoas_envolvidas')
        endereco = request.POST.get('endereco')
        data_documento = request.POST.get('data_documento')
        tamanho_area = request.POST.get('tamanho_area')
        local_armazenamento = request.POST.get('local_armazenamento')

        # Verifique se todos os campos foram preenchidos
        if not (titulo and resumo and pessoas_envolvidas_ids and endereco and data_documento and tamanho_area and local_armazenamento):
            return HttpResponse('Por favor, preencha todos os campos.')

        # Converta IDs de pessoas em instâncias do modelo Pessoa
        pessoas_envolvidas = Pessoa.objects.filter(id__in=pessoas_envolvidas_ids)

        # Lógica para processar os dados do formulário
        try:
            new_documento = Documento.objects.create(
                usuario=request.user,  # Substitua pelo usuário real
                titulo=titulo, 
                resumo=resumo, 
                endereco=endereco,
                data_documento=data_documento, 
                tamanho_area=tamanho_area,
                local_armazenamento=local_armazenamento,
            )
            new_documento.pessoas_envolvidas.set(pessoas_envolvidas)
            new_documento.save()
            return redirect('meus_documentos')
        except Exception as e:
            print(e)
            return HttpResponse('Erro ao registrar o documento.')

    return render(request, 'novo_documento.html', {'pessoas': pessoas})



def meus_documentos(request):
    documentos = Documento.objects.all()
    return render(request, 'meus_documentos.html', {'documentos': documentos})


def excluir_documento(request, documento_id):
    try:
        documento = Documento.objects.get(pk=documento_id)
        documento.delete()
        return redirect('meus_documentos')
    except Documento.DoesNotExist:
        return HttpResponse('Documento não encontrado.')



def pesquisar_documentos(request):
    search_query = request.GET.get('search', '')

    # Realize a pesquisa no banco de dados
    documentos = Documento.objects.filter(
        titulo__icontains=search_query
    ).distinct()

    return render(request, 'meus_documentos.html', {'documentos': documentos, 'search_query': search_query})



def relatorio(request):
    return render(request, 'relatorio_documentos.html')