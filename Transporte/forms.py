from django import forms
from Sistema_Transporte.models import Pasajero, Bus, Ruta, Viaje, Boleto

class PasajeroForm(forms.ModelForm):
    
    class Meta:
        model= Pasajero
        fields= ['nombre', 'identificacion', 'correo']
        
class BusForm(forms.ModelForm):
    
    class Meta:
        model= Bus
        fields= ['placa', 'capacidad']
        
class RutaForm(forms.ModelForm):
    
    class Meta:
        model= Ruta
        fields= ['origen', 'destino','precio']
        
class ViajeForm(forms.ModelForm):
    
    class Meta:
        model= Viaje
        fields= ['fecha','hora','bus','ruta']
        widgets={
            'fecha': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            })
        }
        
class BoletoForm(forms.ModelForm):
    
    class Meta:
        model= Boleto
        fields= ['pasajero', 'viaje', 'no_asiento']