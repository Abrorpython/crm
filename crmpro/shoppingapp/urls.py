from django.urls import path

from .views import shopping_list,shopping_detail
urlpatterns = [
    path('shop/',shopping_list,name = 'shopping'),
    path('shop/<int:pk>/',shopping_detail,name='shopping_detail'),
]