from .utils.data import get_cryptocurrencies_dataframe

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np


def get_coin_figure(coin):
    coin_dataframe = get_cryptocurrencies_dataframe(coin)
    first_time = np.datetime64(coin_dataframe['price_update'][0])
    last_time = np.datetime64(coin_dataframe['price_update'][len(coin_dataframe) - 1])

    low_price = 0
    high_price = 0
    for price in coin_dataframe['price']:
        if float(price) > high_price:
            high_price = float(price)
    high_price *= 2

    dpi = plt.gcf().get_dpi()
    fig, ax = plt.subplots(1, figsize=(1920/float(dpi), 1080/float(dpi)), dpi=dpi)

    ax.plot('price_update', 'price', data=coin_dataframe)

    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))

    plt.xlim(first_time, last_time)
    plt.ylim(low_price, high_price)

    plt.tight_layout()

    return fig


atari_graph = get_coin_figure('atari')
bitcoin_graph = get_coin_figure('bitcoin')
bitcoin_cash_graph = get_coin_figure('bitcoin-cash')
curve_dao_token_graph = get_coin_figure('curve-dao-token')
ethereum_graph = get_coin_figure('ethereum')
fantom_graph = get_coin_figure('fantom')
monero_graph = get_coin_figure('monero')
tarot_graph = get_coin_figure('tarot')
tomb_graph = get_coin_figure('tomb')
