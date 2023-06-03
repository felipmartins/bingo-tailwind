from django.urls import path
from bingo.views import get_a_card, index

urlpatterns = [
    path('', index, name='index'),
    path('card', get_a_card, name='card'),
]