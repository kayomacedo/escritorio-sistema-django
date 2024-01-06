from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User

from documento.models import Documento
from sistema.models import Team, UserProfile

# Create your views here.

# Create your views here.


def index(reques):
    return redirect('login')


def registro_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        team= (f'{username}team')

        # Verifica se todos os campos estão preenchidos
        if not (username and email and password and confirm_password):
            return render(request, 'registro_usuario.html', {'error_message': 'Por favor, preencha todos os campos.'})

        # Verifica se as senhas são iguais
        elif password != confirm_password:
            return render(request, 'registro_usuario.html', {'error_message': 'As senhas não coincidem.'})

        # Verifica se username ou email já existem
        user_exists = User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()

        if user_exists:
            return render(request, 'registro_usuario.html', {'error_message': 'Nome de usuário ou email já estão em uso.'})
        
        # Cria e salva o usuário
        try:
            # Obter ou criar um time (altere 'Nome do Time' conforme necessário)
            team, criado = Team.objects.get_or_create(name=team)
            # Adicionar o usuário ao time
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
             # Crie um UserProfile associado ao usuário e ao time
            perfil = UserProfile.objects.create(user=user, team=team)
            perfil.save()
            return render(request, 'registro_usuario.html', {'success_message': 'Novo usuário registrado!'})
        except Exception as e:
            return render(request, 'registro_usuario.html', {'error_message': f'Erro: {e}'})

    return render(request, 'registro_usuario.html')


def login_usuario(request):
    
    if request.user.is_authenticated:

         return redirect('home')

   
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Verifica se username e password foram fornecidos
        if username and password:
            user = authenticate(request, username=username, password=password)
            print(user)
            # Verifica se o usuário foi autenticado com sucesso
            if user is not None:
                login(request, user)
                # Redireciona para a página desejada após o login (por exemplo, a página inicial)
                return redirect('login')
            else:
                # Se a autenticação falhar, você pode adicionar uma mensagem de erro
                error_message = 'Credenciais inválidas. Por favor, tente novamente.'
        else:
            # Se username ou password não foram fornecidos, você pode adicionar uma mensagem de erro
            error_message = 'Por favor, forneça nome de usuário e senha.'

    return render(request, 'login_usuario.html', {'error_message': error_message if 'error_message' in locals() else ''})

@login_required(login_url='/login/') 
def home(request):
    #peguei o time do usuario logado
    team = request.user.userprofile.team
 
    # Obtenha a contagem real de documentos cadastrados
    numero_de_documentos = Documento.objects.count()  # Ajuste conforme necessário
    meus_documentos = Documento.objects.filter(team=team).count()
    context = {
        'numero_de_documentos': numero_de_documentos,
        'meus_documentos': meus_documentos,
        'team':team.name
    }

    return render(request,'home.html', context)


def logout_sistem(request):
    logout(request)
    return redirect('login')


