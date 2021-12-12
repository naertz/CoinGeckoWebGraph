from django.conf import settings

from .database import Database
from .sql_statements import create_coin_table, delete_coin_table, select_all_from_coin, select_count_from_sqlite_master_where_name, insert_into_coin_all

import datetime
import json
import re
import requests
import pandas as pd


def get_market_chart_response(coin_id, vs_currency, days, interval):
    return requests.get(f'https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart', params={'vs_currency': vs_currency, 'days': days, 'interval': interval})


def get_coin_usd_minutely_prices_in_previous_24_hours(coin):
    return json.loads(get_market_chart_response(coin, 'usd', 1, 'minutely').text)['prices']


def get_coin_usd_timestamps_prices_tuple_list(coin):
    timestamps_prices = []
    for timestamp_price in get_coin_usd_minutely_prices_in_previous_24_hours(coin):
        timestamp = datetime.datetime.utcfromtimestamp(timestamp_price[0] / 1000)
        price = '${:,.10f}'.format(float(timestamp_price[1]))
        timestamps_prices.append((timestamp, price))
    return timestamps_prices


cryptocurrencies_database = Database(settings.BASE_DIR / 'crypto_graphs/databases/cryptocurrencies.db')


def get_cryptocurrencies_dataframe(coin):
    coin_table_name = re.sub('-', '_', coin)
    if not cryptocurrencies_database.fetchonecell(select_count_from_sqlite_master_where_name(coin_table_name)):
        cryptocurrencies_database.execute(create_coin_table(coin_table_name))
    else:
        cryptocurrencies_database.execute(delete_coin_table(coin_table_name))
        cryptocurrencies_database.execute(create_coin_table(coin_table_name))
    cryptocurrencies_database.executemany(insert_into_coin_all(coin_table_name), get_coin_usd_timestamps_prices_tuple_list(coin))
    
    coin_dataframe = pd.read_sql_query(select_all_from_coin(coin_table_name), cryptocurrencies_database.get_connection())
    coin_dataframe['price'] = pd.to_numeric(coin_dataframe['price'].replace('[$,]', '', regex=True))
    coin_dataframe['price_update'] = pd.to_datetime(coin_dataframe['price_update'])
    return coin_dataframe
