from django.urls import path
from . views import sales_list, sales_detail, fura_list, fura_detail

urlpatterns = [
    path('sotuv/', sales_list, name='sotuv'),
    path('sotuv/<int:pk>/', sales_detail, name='sotuv_detail'),
    path('fura/', fura_list, name='fura'),
    path('fura/<int:pk>/', fura_detail, name='fura_detail'),
]
