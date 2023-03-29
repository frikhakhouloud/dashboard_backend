
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    #on fait applel au urls de l'application filtre
    path('',include('filtre.urls'))
]
