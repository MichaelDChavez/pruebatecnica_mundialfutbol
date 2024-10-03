from django.contrib import admin
from .models import Equipos
from .models import Jugadores
from .models import Nacionalidad
from .models import Entrenadores

admin.site.register(Equipos)
admin.site.register(Jugadores)
admin.site.register(Nacionalidad)
admin.site.register(Entrenadores)
