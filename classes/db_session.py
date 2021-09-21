import sqlite3

def connectdb(path):
    try:
        con = sqlite3.connect(path)
    except:
        con = None
    return con

