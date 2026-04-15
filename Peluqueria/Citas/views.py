from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.http import JsonResponse
from django.utils.dateparse import parse_datetime

from .models import Cita, Profesional, Servicio

# vistas.
@login_required
def index(request):
    return render(request, 'paginas/index.html')

def Login(request):
    return render(request, 'paginas/login.html')

@login_required
def listarCitas(request):
    citas = Cita.objects.all()
    return render(request, 'cita/inicio.html', {'citas': citas})

@login_required
def agregarCita(request):
    servicios = Servicio.objects.all()
    profesionales = Profesional.objects.all()

    if request.method == "POST":
        servicio_id = request.POST.get("servicio")
        profesional_id = request.POST.get("profesional")
        fecha_cita = request.POST.get("fecha_cita")
        prioridad = request.POST.get("prioridad")

        if servicio_id and profesional_id and fecha_cita and prioridad:
            Cita.objects.create(
                servicio_id=servicio_id,
                profesional_id=profesional_id,
                fecha_cita=fecha_cita,
                prioridad=prioridad
            )
            messages.success(request, "Cita creada correctamente.")
            return redirect("cita")

    return render(request, "cita/crear.html", {
        "servicios": servicios,
        "profesionales": profesionales
    })

@login_required
def editarCita(request, id):
    cita = get_object_or_404(Cita, id=id)
    servicios = Servicio.objects.all()
    profesionales = Profesional.objects.all()

    if request.method == "POST":
        servicio_id = request.POST.get("servicio")
        profesional_id = request.POST.get("profesional")
        fecha_cita = request.POST.get("fecha_cita")
        prioridad = request.POST.get("prioridad")

        fecha_parseada = parse_datetime(fecha_cita)

        cita.servicio_id = servicio_id
        cita.profesional_id = profesional_id
        cita.fecha_cita = fecha_parseada
        cita.prioridad = prioridad
        cita.save()

        messages.success(request, "Cita actualizada.")
        return redirect("cita")

    return render(request, "cita/editar.html", {
        "cita": cita,
        "servicios": servicios,
        "profesionales": profesionales
    })

@login_required
def eliminarCita(request, id):
    cita = get_object_or_404(Cita, id=id)

    if request.method == 'POST':
        cita.delete()
        messages.success(request, "Cita eliminada.")
        return redirect('cita')

    return render(request, 'cita/eliminar.html', {'cita': cita})

def iniciarSesion(request):
    if request.method == 'POST':
        username = request.POST.get('Usuarios')
        password = request.POST.get('password')

        # Autenticar con el sistema de Django
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'paginas/login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'paginas/login.html')

def Registro(request):
    if request.method == 'POST':
        username = request.POST.get('Usuarios')
        password = request.POST.get('password')
        role = request.POST.get('role')

        print("USERNAME:", username)
        print("PASSWORD:", password)
        print("ROLE:", role)

        if not username or not password or not role:
            messages.error(request, "Faltan datos.")
            return redirect('login')

        if User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ya existe.")
            return redirect('login')
        
        user = User.objects.create_user(
            username=username,
            password=password
        )

        print("USUARIO CREADO")

        grupo, created = Group.objects.get_or_create(name=role)
        user.groups.add(grupo)
        user.save()

        messages.success(request, "Usuario registrado correctamente.")
        return redirect('login')

    return redirect('login')
        
@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')

@login_required
def agregarProfesional(request):
    servicios = Servicio.objects.all()

    if request.method == "POST":
        nombre = request.POST.get("nombre")
        usuario_id = request.POST.get("usuario")
        servicios_ids = request.POST.getlist("servicios")

        if not nombre:
            messages.error(request, "El nombre es obligatorio.")
            return redirect("agregarProfesional")

        profesional = Profesional.objects.create(nombre=nombre, usuario_id=usuario_id)
        profesional.servicios.set(servicios_ids)

        messages.success(request, "Profesional creado.")
        return redirect("cita")

    return render(request, "profesional/crearpro.html", {
        "servicios": servicios,
        "users": User.objects.all()
    })

@login_required
def agregarServicio(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        precio = request.POST.get("precio")

        if not nombre or not precio:
            messages.error(request, "Todos los campos son obligatorios.")
            return redirect("agregarServicio")

        Servicio.objects.create(nombre=nombre, precio=precio)

        messages.success(request, "Servicio creado.")
        return redirect("cita")

    return render(request, "servicio/crearser.html")

@login_required
def obtener_profesionales(request):
    servicio_id = request.GET.get('servicio_id')

    if not servicio_id:
        return JsonResponse([], safe=False)

    profesionales = Profesional.objects.filter(servicios__id=servicio_id)

    data = list(profesionales.values('id', 'nombre'))

    return JsonResponse(data, safe=False)



# @login_required
# def verificar_url_view(request):
#     resultado = None

#     if request.method == "POST":
#         url = request.POST.get("url")

#         if not url:
#             messages.error(request, "Debe ingresar una URL.")
#             return redirect("verificar_url")

#         resultado = verificar_url_django(url)

#     return render(request, "paginas/verificar_url.html", {"resultado": resultado})

# def verificar_url_django(url):
#     datos = {
#         "url_original": url,
#         "https": False,
#         "redirecciones": [],
#         "url_final": None,
#         "codigo": None,
#         "error": None,
#     }

#     try:
#         response = requests.get(url, allow_redirects=True, timeout=5)

#         datos["https"] = url.startswith("https://")

#         if response.history:
#             for r in response.history:
#                 datos["redirecciones"].append({
#                     "desde": r.url,
#                     "hacia": r.next.url if r.next else r.headers.get("Location", "Desconocido"),
#                     "codigo": r.status_code
#                 })

#         datos["url_final"] = response.url
#         datos["codigo"] = response.status_code

#     except requests.exceptions.RequestException as e:
#         datos["error"] = str(e)

#     return datos