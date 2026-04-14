from django.contrib import messages
from Sistema_Transporte.models import Bus,Pasajero,Viaje,Ruta,Boleto
from django.shortcuts import render, redirect
from .forms import PasajeroForm, BusForm, RutaForm, ViajeForm, BoletoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm

def bus(request):
    form= BusForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('Bus')
    
    return render(request, 'Bus.html', {'form':form})

def pasajero(request):
    form = PasajeroForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('pasajero')
    return render(request, 'Pasajero.html', {'form': form})



def viaje(request):
    form = ViajeForm(request.POST or None)
    
    if form.is_valid():
        datos= form.cleaned_data
        viaje_existe= Viaje.objects.filter(bus=datos['bus'], fecha=datos['fecha'], hora=datos['hora']).first()
        if viaje_existe:
            messages.error(request, 'El Bus tiene el horario ocupado')
            return redirect('viaje')
        else:
            messages.success(request, 'Se finalizo el Viaje')
            form.save()
            
            return redirect('viaje')
        
    return render(request, 'Viaje.html', {'form':form})


def ruta(request):
    form = RutaForm(request.POST or None)
    
    if form.is_valid():
        
        form.save()
        return redirect('ruta')
    
    return render(request, 'Ruta.html', {'form': form})



def boleto(request):
    form = BoletoForm(request.POST or None)
    buscando= Boleto.objects.all()
    
    if form.is_valid():
        datos = form.cleaned_data
        boleto_existente = Boleto.objects.filter(viaje=datos['viaje'],no_asiento=datos['no_asiento']).first
        buscando= Boleto.objects.filter(viaje=datos['viaje'])
        
        if boleto_existente:
            messages.error(request,'Este numero de boleto ya existe')
            return redirect('boleto')
        
        else:
            messages.success(request, 'Pase adelante, ¡Feliz Viaje!')
        form.save()
        return redirect('boleto')
    
    return render(request, 'Boleto.html', {'form': form , 'boleto': buscando})


def cerrar_sesion(request):
    logout(request)
    return redirect('login')

def registrar_usuario(request):
    form = UserCreationForm(request.POST)
    
    if form.is_valid():
        form.save()
        return redirect('login')
    
    return render(request,'registro_usuario.html',{'form':form})
    