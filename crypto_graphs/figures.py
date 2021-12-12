from .utils.data import get_cryptocurrencies_dataframe

from matplotlib.dates import DateFormatter
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
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

    plt.style.use('dark_background')

    dpi = plt.gcf().get_dpi()
    fig, ax = plt.subplots(1, figsize=(1600/float(dpi), 900/float(dpi)), dpi=dpi)

    ax.plot('price_update', 'price', data=coin_dataframe, color='white')

    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d %H:%M'))
    ax.yaxis.set_major_formatter(StrMethodFormatter('${x:,.2f}'))

    plt.xlim(first_time, last_time)
    plt.ylim(low_price, high_price)

    plt.tight_layout()

    return fig


atari = get_coin_figure('atari')
bitcoin = get_coin_figure('bitcoin')
bitcoin_cash = get_coin_figure('bitcoin-cash')
curve_dao_token = get_coin_figure('curve-dao-token')
ethereum = get_coin_figure('ethereum')
fantom = get_coin_figure('fantom')
monero = get_coin_figure('monero')
tarot = get_coin_figure('tarot')
tomb = get_coin_figure('tomb')
