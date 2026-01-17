from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    TIPOS_USUARIO = (
        ("cliente", "Cliente"),
        ("transportista", "Transportista"),
        ("admin", "Administrador"),
    )

    tipo = models.CharField(max_length=20, choices=TIPOS_USUARIO, default="cliente")
    direccion = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.username