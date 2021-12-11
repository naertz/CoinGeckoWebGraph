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
    url('fantom_graph/', crypto_graphs_view.fantom_view, name='Fantom Graph'),
    url('atari_graph/', crypto_graphs_view.atari_view, name='Atari Graph'),
    url('tarot_graph/', crypto_graphs_view.tarot_view, name='Tarot Graph'),
]
