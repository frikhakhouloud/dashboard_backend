from django.urls import path, include
from filtre import views
# from rest_framework import routers
# from filtre.views import DivisionSet
from django.urls import re_path

""" router = routers.DefaultRouter()
router.register('division', DivisionSet)
 """

urlpatterns = [
    path('division/',views.division_list,name='home'),
    path('profit/',views.profit_list,name='home'),
    path('organisation/',views.organisation_list,name='home'),
    path('range/',views.filter_range,name='home'),

    # re_path('divisionAPI/$',views.DivisionAPI),
    # re_path('divisionAPI/',views.DivisionAPI), 



    path ('division/<int:id>/',views.division_details,name='division_details'),

]