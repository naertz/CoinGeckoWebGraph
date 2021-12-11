from django.shortcuts import render

from .figures import atari_graph, fantom_graph, tarot_graph

import io
import base64
import urllib

# Create your views here.


def fantom_view(request):
    fig = fantom_graph

    buffer = io.BytesIO()
    fig.savefig(buffer, format="png")
    buffer.seek(0)
    string = base64.b64encode(buffer.read())
    uri = urllib.parse.quote(string)
    return render(request, 'fantom_graph.html', {'data':uri})


def atari_view(request):
    fig = atari_graph

    buffer = io.BytesIO()
    fig.savefig(buffer, format="png")
    buffer.seek(0)
    string = base64.b64encode(buffer.read())
    uri = urllib.parse.quote(string)
    return render(request, 'atari_graph.html', {'data':uri})


def tarot_view(request):
    fig = tarot_graph

    buffer = io.BytesIO()
    fig.savefig(buffer, format="png")
    buffer.seek(0)
    string = base64.b64encode(buffer.read())
    uri = urllib.parse.quote(string)
    return render(request, 'tarot_graph.html', {'data':uri})