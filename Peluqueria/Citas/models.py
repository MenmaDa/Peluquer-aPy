from django.db import models


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


class Profesional(models.Model):
    nombre = models.CharField(max_length=100)
    servicios = models.ManyToManyField(Servicio, related_name="profesionales")
    usuario = models.OneToOneField('auth.User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre


class Cita(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE)
    fecha_cita = models.DateTimeField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    prioridad = models.CharField(
        max_length=10,
        choices=[
            ('alta', 'Alta'),
            ('media', 'Media'),
            ('baja', 'Baja')
        ]
    )

    def __str__(self):
        return f"{self.servicio} - {self.profesional}"