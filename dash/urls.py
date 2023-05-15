
from django.contrib import admin
from django.urls import path,include
# from filtre.urls import router as filtre_router
# from rest_framework import routers
#from django.conf.urls import url
from django.urls import re_path
admin.site.site_header = "Dashboard Admin"
admin.site.site_title = "Dashboard Admin Portal"
admin.site.index_title = "Welcome to Dashboard Researcher Portal"




""" router = routers.DefaultRouter()
router.registry.extend(filtre_router.registry)
 """

urlpatterns = [
    path('admin/', admin.site.urls),
   # re_path(r'^',include('filtre.urls')),

    #on fait applel au urls de l'application filtre
    path('filtre/',include('filtre.urls')),
    path('order/',include('order_past.urls')),

    # path('api',include(router.urls))
]


# endpoint = 'http://127.0.0.1:8000/api'