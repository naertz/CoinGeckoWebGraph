from django.shortcuts import render

import io

from .figures import atari_graph, bitcoin_cash_graph, bitcoin_graph, curve_dao_token_graph, ethereum_graph, fantom_graph, monero_graph, tarot_graph, tomb_graph

# Create your views here.


def atari_view(request):
    fig = atari_graph
    buffer = io.BytesIO()
    fig.savefig(buffer, format='svg')
    buffer.seek(0)
    figure_data = buffer.read().decode('utf-8')
    return render(request, 'atari_graph.html', {'data': figure_data})


def bitcoin_view(request):
    fig = bitcoin_graph
    buffer = io.BytesIO()
    fig.savefig(buffer, format='svg')
    buffer.seek(0)
    figure_data = buffer.read().decode('utf-8')
    return render(request, 'bitcoin_graph.html', {'data': figure_data})


def bitcoin_cash_view(request):
    fig = bitcoin_cash_graph
    buffer = io.BytesIO()
    fig.savefig(buffer, format='svg')
    buffer.seek(0)
    figure_data = buffer.read().decode('utf-8')
    return render(request, 'bitcoin_cash_graph.html', {'data': figure_data})


def curve_dao_token_view(request):
    fig = curve_dao_token_graph
    buffer = io.BytesIO()
    fig.savefig(buffer, format='svg')
    buffer.seek(0)
    figure_data = buffer.read().decode('utf-8')
    return render(request, 'curve_dao_token_graph.html', {'data': figure_data})


def ethereum_view(request):
    fig = ethereum_graph
    buffer = io.BytesIO()
    fig.savefig(buffer, format='svg')
    buffer.seek(0)
    figure_data = buffer.read().decode('utf-8')
    return render(request, 'ethereum_graph.html', {'data': figure_data})


def fantom_view(request):
    fig = fantom_graph
    buffer = io.BytesIO()
    fig.savefig(buffer, format='svg')
    buffer.seek(0)
    figure_data = buffer.read().decode('utf-8')
    return render(request, 'fantom_graph.html', {'data': figure_data})


def monero_view(request):
    fig = monero_graph
    buffer = io.BytesIO()
    fig.savefig(buffer, format='svg')
    buffer.seek(0)
    figure_data = buffer.read().decode('utf-8')
    return render(request, 'monero_graph.html', {'data': figure_data})


def tarot_view(request):
    fig = tarot_graph
    buffer = io.BytesIO()
    fig.savefig(buffer, format='svg')
    buffer.seek(0)
    figure_data = buffer.read().decode('utf-8')
    return render(request, 'tarot_graph.html', {'data': figure_data})


def tomb_view(request):
    fig = tomb_graph
    buffer = io.BytesIO()
    fig.savefig(buffer, format='svg')
    buffer.seek(0)
    figure_data = buffer.read().decode('utf-8')
    return render(request, 'tomb_graph.html', {'data': figure_data})
