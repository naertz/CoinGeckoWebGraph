"""CoinGecko_Web_Graph URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from crypto_graphs import views as crypto_graphs_view

urlpatterns = [
    path('admin/', admin.site.urls),
    url('atari_graph/', crypto_graphs_view.atari_view, name='Atari Graph'),
    url('bitcoin_graph/', crypto_graphs_view.bitcoin_view, name='Bitcoin Graph'),
    url('bitcoin_cash_graph/', crypto_graphs_view.bitcoin_cash_view, name='Bitcoin Cash Graph'),
    url('curve_dao_token_graph/', crypto_graphs_view.curve_dao_token_view, name='Curve DAO Token Graph'),
    url('ethereum_graph/', crypto_graphs_view.ethereum_view, name='Ethereum Graph'),
    url('fantom_graph/', crypto_graphs_view.fantom_view, name='Fantom Graph'),
    url('monero_graph/', crypto_graphs_view.monero_view, name='Monero Graph'),
    url('tarot_graph/', crypto_graphs_view.tarot_view, name='Tarot Graph'),
    url('tomb_graph/', crypto_graphs_view.tomb_view, name='Tomb Graph'),
]
