"""
Program:               database.py
Author:                Noah Allan Ertz
Last Date Modified:    2021-12-03

Database class
"""

import sqlite3 as lite


class Database:
    def __init__(self, database_name):
        self._database_name = database_name
        self._connection = self.set_connection()

    def __del__(self):
        self._connection.close()

    def set_connection(self):
        try:
            connection = lite.connect(self._database_name)
            return connection
        except lite.Error as err:
            print(err)

    def get_connection(self):
        return self._connection

    def connect(self):
        try:
            self._connection = lite.connect(self._database_name)
        except lite.Error as err:
            print(err)

    def execute(self, statement, values=None, execute_type=0):
        try:
            cursor = self._connection.cursor()
            if values is None:
                cursor.execute(statement)
            else:
                if execute_type == 0:
                    cursor.execute(statement, values)
                else:
                    cursor.execute(statement % values)
            cursor.close()
            self._connection.commit()
        except lite.Error as err:
            print(err)

    def executemany(self, statement, values):
        try:
            cursor = self._connection.cursor()
            cursor.executemany(statement, values)
            cursor.close()
            self._connection.commit()
        except lite.Error as err:
            print(err)

    def fetchonecell(self, statement, values=None):
        if values is None:
            cell = self.fetchonerow(statement)[0]
        else:
            cell = self.fetchonerow(statement, values)[0]
        return cell

    def fetchonerow(self, statement, values=None, execute_type=0):
        try:
            cursor = self._connection.cursor()
            if values is None:
                cursor.execute(statement)
            else:
                if execute_type == 0:
                    cursor.execute(statement, values)
                else:
                    cursor.execute(statement % values)
            row = cursor.fetchone()
            cursor.close()
            return row
        except lite.Error as err:
            print(err)
        return None

    def fetchallcells(self, statement, values=None):
        cells = []
        if values is None:
            for row in self.fetchallrows(statement):
                cells.append(row[0])
        else:
            for row in self.fetchallrows(statement, values):
                cells.append(row[0])
        return cells

    def fetchallrows(self, statement, values=None, execute_type=0):
        try:
            cursor = self._connection.cursor()
            if values is None:
                cursor.execute(statement)
            else:
                if execute_type == 0:
                    cursor.execute(statement, values)
                else:
                    cursor.execute(statement % values)
            rows = cursor.fetchall()
            cursor.close()
            return rows
        except lite.Error as err:
            print(err)
        return None
