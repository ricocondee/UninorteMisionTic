import sqlite3

def getDb():
    con = sqlite3.connect('database.db')
    return con

def closeDb():
    con = getDb()
    con = con.close()
    return con