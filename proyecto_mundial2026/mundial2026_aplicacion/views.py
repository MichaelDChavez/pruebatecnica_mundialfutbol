from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib import messages
from .forms import RegistroForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.db import transaction
from django.contrib.auth.decorators import login_required
from .models import Equipos, Jugadores, Entrenadores


def home(request):
    return render(request, 'home.html')

@login_required(login_url='/login/')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='/login/')
def calendario (request):
    return render(request, 'calendario.html')

@login_required(login_url='/login/')
def equipos(request):
    equipos = Equipos.objects.all()  
    return render(request, 'equipos.html', {
        "equipos": equipos
    })

@login_required(login_url='/login/')
def jugadores(request):
    jugadores = Jugadores.objects.all()
    return render(request, 'jugadores.html', {
        "jugadores": jugadores
    })

def login(request):
    if request.method == "POST":
        username = request.POST.get("usuario")
        password = request.POST.get("password")

        # Autenticación
        user = authenticate(username=username, password=password)
        if user is not None:
            django_login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
    
    return render(request, 'login.html')

def logout(request):
    django_logout(request)
    messages.success(request, 'Has cerrado sesión con exito')
    return redirect('login')

@login_required(login_url='/login/')
def perfil(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = CustomUserChangeForm(instance=request.user)

    seleccione

    return render(request, 'perfil.html', {"form": form})

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            django_login(request, user)
            messages.success(request, 'Te has registrado exitosamente.')
            return redirect('login')
        else:
            messages.error(request, 'Por favor corrige los errores.')
    else:
        form = RegistroForm()
    
    return render(request, 'registro.html', {'form': form})

@login_required(login_url='/login/')
def tecnicos (request):
    tecnicos = Entrenadores.objects.prefetch_related('seleccion').all()
    return render(request, 'tecnicos.html', {
        "tecnicos": tecnicos
    })
