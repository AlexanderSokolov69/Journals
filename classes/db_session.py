import sqlite3
import sys
from configparser import ConfigParser

def connectdb(path=''):
    try:
        cfg = ConfigParser()
        cfg.read("settings.ini")
        path = cfg.get("Settings", "db_path")
    except:
        print('settings.ini where?')
    try:
        con = sqlite3.connect(path)
        print('Подключена БД:',  path)
    except (sqlite3.Error, sqlite3.Warning) as err:
        print(err, path)
        sys.exit()
    return con

