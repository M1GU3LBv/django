from django.db import models

# Create your models here.
from django.db import models


# Create your models here.


class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    foto_url = models.URLField()
    telefono = models.CharField(max_length=50)
    email = models.EmailField()
    direccion = models.CharField(max_length=50)
    tipo_documento = models.ForeignKey("TipoDocumento", on_delete=models.CASCADE)
    documento_identidad = models.CharField(max_length=11)
    estado = models.BooleanField(default=True)


class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)


class Usuario(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    persona = models.ForeignKey("Persona", on_delete=models.CASCADE)
    rol = models.ForeignKey("Rol", on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)


class Rol(models.Model):
    nombre = models.CharField(max_length=50)
    privilegios = models.ForeignKey("Privilegios", on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)


class RolPrivilegios(models.Model):
    Rol = models.ForeignKey("Rol", on_delete=models.CASCADE)
    Privilegios = models.ForeignKey("Privilegios", on_delete=models.CASCADE)


class Privilegios(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)


class Reserva(models.Model):
    fecha_reserva = models.DateField()
    hora_reserva = models.TimeField()
    persona = models.ForeignKey("Persona", on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    estado = models.BooleanField(default=False)


# class Confirmacion_pago(models.Model):
#     fecha_pago = models.DateField()
#     monto = models.FloatField()
#     reserva = models.ForeignKey("Reserva", on_delete=models.CASCADE)
#     fecha_creacion = models.DateField(auto_now_add=True)
#     fecha_modificacion = models.DateField(auto_now=True)
#     estado = models.BooleanField(default=True)


class Detalle(models.Model):
    monto = models.FloatField()
    reserva = models.ForeignKey("Reserva", on_delete=models.CASCADE)
    usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    Descuento = models.ForeignKey("Descuento", on_delete=models.CASCADE)
    Vuelo = models.ForeignKey("Vuelo", on_delete=models.CASCADE)
    url_pago = models.URLField()
    url_reserva = models.URLField()
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificacion = models.DateField(auto_now=True)
    estado = models.BooleanField(default=True)


class Vuelo(models.Model):
    tipo = models.CharField(max_length=50)
    precio = models.FloatField()
    estado = models.BooleanField(default=True)


class Descuento(models.Model):
    codigo = models.CharField(max_length=50)
    fecha_fin = models.DateField()
    fecha_inicio = models.DateField()
    porcentaje = models.FloatField()
    estado = models.BooleanField(default=True)
