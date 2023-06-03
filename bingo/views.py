from django.shortcuts import render
import requests


def index(request):
    context = {}
    return render(request, 'index.html')

def get_a_card(request):
    bingo_card = requests.get("http://bingo-api.com.br/card/").json()['card_values']
    context = {"card": enumerate(bingo_card), 'last_row_index': len(bingo_card)-1, 'rows': len(bingo_card)}
    return render(request, 'card.html', context)
