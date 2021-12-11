"""
Program:               sql_statements.py
Author:                Noah Allan Ertz
Last Date Modified:    2021-12-03

SQL statements
"""

"""CREATE TABLE Statements"""


def create_coin_table(coin):
    return f'''CREATE TABLE IF NOT EXISTS {coin} (
                   price_update timestamp NOT NULL,
                   price        float     NOT NULL
               );'''


"""DROP TABLE Statements"""


def delete_coin_table(coin):
    return f'''DROP TABLE {coin};'''


"""INSERT Statements"""


def insert_into_coin_all(coin):
    return f'''INSERT INTO {coin} (price_update, price)
               VALUES (?, ?);'''


"""SELECT Statements"""
def select_count_from_sqlite_master_where_name(coin):
    return f'''SELECT COUNT(*) FROM sqlite_master WHERE name='{coin}';'''


def select_all_from_coin(coin):
    return f'''SELECT * FROM {coin};'''
