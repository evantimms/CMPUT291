import sqlite3
import sys

def createTable(c):
    schema = open('./CreateTables.sql', 'r').read()
    c.executescript(schema)

def populate(c):
    data = open('./Data.sql', 'r').read()
    c.executescript(data)

def runSetup():
    args = sys.argv
    if len(args) > 1:
        db = ":memory:" if "--usemem" in args else args[1]
    else:
        raise Exception("Missing argument for table name. Pass --usemem for an in memory db or a db name")
    
    print("using table: {}".format(db))
    conn = sqlite3.connect(db) # change to :memory: to use in mem database (refreshes everytime)
    c = conn.cursor()

    createTable(c)
    print('table created')
    populate(c)
    print('populated table')
    return c
