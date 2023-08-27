from django.urls import path
from . import views

urlpatterns = [
    path('balance/<str:address>', views.ethereum_balance, name='balance')
]
