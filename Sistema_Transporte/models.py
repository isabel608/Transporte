from django.db import models

# Create your models here.
class Bus(models.Model):
    placa= models.CharField(max_length=8, unique=True)
    capacidad=models.IntegerField()
    
class Pasajero(models.Model):
    nombre=models.CharField(max_length=30)
    identificacion=models.CharField(max_length=13,unique=True)
    correo=models.EmailField()
    
class Ruta(models.Model):
    origen=models.CharField(max_length=30)
    destino=models.CharField(max_length=30)
    precio=models.DecimalField(max_digits=10,decimal_places=2)
    
class Viaje(models.Model):
    fecha=models.DateField()
    hora=models.TimeField()
    bus=models.ForeignKey(Bus,on_delete=models.CASCADE)
    ruta=models.ForeignKey(Ruta,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.ruta.origen
    
    
class Boleto(models.Model):
    pasajero=models.ForeignKey(Pasajero,on_delete=models.CASCADE)
    viaje=models.ForeignKey(Viaje,on_delete=models.CASCADE)
    no_asiento=models.CharField()