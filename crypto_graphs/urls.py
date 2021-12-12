from django.urls import path
from . import views

urlpatterns = [
    path('atari_graph/', views.atari_view),
    path('bitcoin_graph/', views.bitcoin_view),
    path('bitcoin_cash_graph/', views.bitcoin_cash_view),
    path('curve_dao_token_graph/', views.curve_dao_token_view),
    path('ethereum_graph/', views.ethereum_view),
    path('fantom_graph/', views.fantom_view),
    path('monero_graph/', views.monero_view),
    path('tarot_graph/', views.tarot_view),
    path('tomb_graph/', views.tomb_view)
]
