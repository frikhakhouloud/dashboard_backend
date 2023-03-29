from django.urls import path, include
from filtre import views
urlpatterns = [
    path('division/',views.division_list,name='home'),
    path('profit/',views.profit_list,name='home'),
    path('organisation/',views.organisation_list,name='home'),
    path('range/',views.filter_range,name='home'),



    path ('division/<int:id>/',views.division_details,name='division_details'),

]