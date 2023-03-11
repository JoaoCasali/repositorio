from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Comentario


@login_required
def Cadastro(request):
    if request.method == "GET":
        return render(request, 'comentarios/cadastro.html')

    resumo = request.POST.get('resumo')
    categoria = int(request.POST.get('categoria'))
    descricao = request.POST.get('descricao')

    usuario = request.user

    comentario = Comentario(resumo = resumo, descricao = descricao, topico= categoria, cidadao= usuario)

    comentario.save()

    return redirect('home')


def Listagem(request):
    List = Comentario.objects.all()
    return render(request, 'comentarios/listagem.html', {'List': List})