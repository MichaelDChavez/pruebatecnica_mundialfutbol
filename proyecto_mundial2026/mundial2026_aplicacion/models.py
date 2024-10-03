from django.db import models

class Equipos(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    bandera = models.ImageField(upload_to='banderas/', null=True, verbose_name='FotoBandera')
    escudo = models.ImageField(upload_to='escudos/', null=True, verbose_name='FotoEscudo')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Equipo"
        verbose_name_plural = "Equipos"
        db_table = "equipos"
        ordering = ['id']


class Jugadores(models.Model):
    PORTERO = 'P'
    DEFENSA = 'D'
    CENTROCAMPISTA = 'C'
    DELANTERO = 'D'

    POSITION_CHOICES = [
        (PORTERO, 'Portero'),
        (DEFENSA, 'Defensa'),
        (CENTROCAMPISTA, 'Centrocampista'),
        (DELANTERO, 'Delantero'),
    ]

    name = models.CharField(max_length=200, verbose_name="Nombre")
    lastname = models.CharField(max_length=200, verbose_name="Apellido")
    picture = models.ImageField(upload_to='jugador/', null=True, verbose_name='FotoJugador')
    birthday = models.DateField(verbose_name="Nacimiento")
    position = models.CharField(max_length=1, choices=POSITION_CHOICES, default=DELANTERO, verbose_name="Posicion")
    number = models.PositiveIntegerField(default=1, verbose_name="numero")
    titular = models.BooleanField(default=True, verbose_name="titular")
    team = models.ForeignKey(Equipos, on_delete=models.CASCADE, verbose_name="equipo")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Jugador"
        db_table = "jugadores"
        ordering = ['id']

class Nacionalidad(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Entrenadores(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    lastname = models.CharField(max_length=200, verbose_name="Apellido")
    picture = models.ImageField(upload_to='director/', null=True, verbose_name='FotoDirector')
    birthday = models.DateField(verbose_name="Nacimiento")
    rol = models.CharField(max_length=100, verbose_name="Rol")
    seleccion = models.ManyToManyField(Equipos, verbose_name="seleccion")
    nacionalidad = models.ForeignKey(Nacionalidad, on_delete=models.CASCADE, verbose_name="nacionalidad")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Entrenador"
        db_table = "entrenadores"
        ordering = ['id']