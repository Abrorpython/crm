from django.urls import path
from .views import (table_list, table_detail,origin_list,
                    origin_detail,accountnumber_list,accountnumber_detail,
                    month_list,month_detail,counterpart_list,counterparty_detail,
                    employes_list,employes_detail,rawmaterial_list,
                    rawmaterial_detail,productname_list,productname_detail,
                    endvalue,)

urlpatterns = [
    path('endvalue/',endvalue,name='endvalue'),
    path('table/',table_list, name='list'),
    path('table/<int:pk>/',table_detail,name='table_detail'),
    path('origin/',origin_list),
    path('origin/<int:pk>/',origin_detail),
    path('accountnumber/',accountnumber_list),
    path('accountnumber/<int:pk>/',accountnumber_detail),
    path('month/',month_list),
    path('month/<int:pk>/',month_detail),
    path('counter/',counterpart_list),
    path('counter/<int:pk>/',counterparty_detail),
    path('employes/',employes_list),
    path('employes/<int:pk>/',employes_detail),
    path('raw/',rawmaterial_list),
    path('raw/<int:pk>/',rawmaterial_detail),
    path('productname/',productname_list),
    path('productname/<int:pk>/',productname_detail),
]
