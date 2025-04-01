import sqlite3


def con():
    con = sqlite3.connect("TeacherdleDB.db")
    return con
def cur():
    a =con()
    cur = a.cursor()
    return cur