from django.conf import settings
from django.shortcuts import render

from . import figures as fig

# Create your views here.


def atari_view(request):
    figure = fig.atari
    figure.savefig(settings.BASE_DIR / 'crypto_graphs/static/svg/atari_graph.svg', format='svg')
    return render(request, 'atari_graph.html')


def bitcoin_view(request):
    figure = fig.bitcoin
    figure.savefig(settings.BASE_DIR / 'crypto_graphs/static/svg/bitcoin_graph.svg', format='svg')
    return render(request, 'bitcoin_graph.html')


def bitcoin_cash_view(request):
    figure = fig.bitcoin_cash
    figure.savefig(settings.BASE_DIR / 'crypto_graphs/static/svg/bitcoin_cash_graph.svg', format='svg')
    return render(request, 'bitcoin_cash_graph.html')


def curve_dao_token_view(request):
    figure = fig.curve_dao_token
    figure.savefig(settings.BASE_DIR / 'crypto_graphs/static/svg/curve_dao_token_graph.svg', format='svg')
    return render(request, 'curve_dao_token_graph.html')


def ethereum_view(request):
    figure = fig.ethereum
    figure.savefig(settings.BASE_DIR / 'crypto_graphs/static/svg/ethereum_graph.svg', format='svg')
    return render(request, 'ethereum_graph.html')


def fantom_view(request):
    figure = fig.fantom
    figure.savefig(settings.BASE_DIR / 'crypto_graphs/static/svg/fantom_graph.svg', format='svg')
    return render(request, 'fantom_graph.html')


def monero_view(request):
    figure = fig.monero
    figure.savefig(settings.BASE_DIR / 'crypto_graphs/static/svg/monero_graph.svg', format='svg')
    return render(request, 'monero_graph.html')


def tarot_view(request):
    figure = fig.tarot
    figure.savefig(settings.BASE_DIR / 'crypto_graphs/static/svg/tarot_graph.svg', format='svg')
    return render(request, 'tarot_graph.html')


def tomb_view(request):
    figure = fig.tomb
    figure.savefig(settings.BASE_DIR / 'crypto_graphs/static/svg/tomb_graph.svg', format='svg')
    return render(request, 'tomb_graph.html')
