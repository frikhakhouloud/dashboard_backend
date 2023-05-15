from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns =[
    #path('',views.getData),
    path('savefile',views.save_file),
    path('selectfile/year/<int:year>/week/<int:week>', views.select_files),
    # path('cclientsave/year/<int:year>/week/<int:week>',views.cclient_save)
    path('count/',views.count),
    path('cost/',views.cost),
    path('count_order_par_division/',views.count_order_par_division),
    path('order_par_organisme/',views.order_par_organisme),
    path('order_par_cp/',views.order_par_cp),
    path('order_par_errors/',views.order_par_errors),








 ] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)