import sqlite3
import sys
import os

def connectdb(path):
    try:
        con = sqlite3.connect(path)
        print('Подключена БД:',  path)
    except (sqlite3.Error, sqlite3.Warning) as err:
        print(err, path)
        sys.exit()
    return con

