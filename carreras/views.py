from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Carrera
from .forms import CarreraForm


def inicio(request):
    return render(request, 'carreras/inicio.html')

@login_required
def lista_carreras(request):
    carreras = Carrera.objects.all().order_by('nombre')
    return render(request, 'carreras/lista.html', {
        'carreras': carreras
    })


@login_required
def crear_carrera(request):
    if request.method == 'POST':
        form = CarreraForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('lista_carreras')
    else:
        form = CarreraForm()

    return render(request, 'carreras/crear.html', {
        'form': form
    })

@login_required
def editar_carrera(request, id):
    carrera = get_object_or_404(Carrera, id=id)

    if request.method == 'POST':
        form = CarreraForm(request.POST, instance=carrera)

        if form.is_valid():
            form.save()
            return redirect('lista_carreras')
    else:
        form = CarreraForm(instance=carrera)

    return render(request, 'carreras/editar.html', {
        'form': form,
        'carrera': carrera
    })


@login_required
def eliminar_carrera(request, id):
    carrera = get_object_or_404(Carrera, id=id)

    if request.method == 'POST':
        carrera.delete()
        return redirect('lista_carreras')

    return render(request, 'carreras/eliminar.html', {
        'carrera': carrera
    })