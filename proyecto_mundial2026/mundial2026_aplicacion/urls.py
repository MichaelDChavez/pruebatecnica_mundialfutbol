from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, index, logout, calendario, equipos, jugadores, login, perfil, registro, tecnicos

urlpatterns = [
    path('', home, name='home'),      
    path('index/', index, name='index'),  
    path('calendario/', calendario, name='calendario'),  
    path('equipos/', equipos, name='equipos'),  
    path('jugadores/', jugadores, name='jugadores'),  
    path('login/', login, name='login'),  
    path('logout/', logout, name='logout'),
    path('perfil/', perfil, name='perfil'),
    path('registro/', registro, name='registro'),  
    path('tecnicos/', tecnicos, name='tecnicos'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)