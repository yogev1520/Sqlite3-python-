#doc type python 3 v3.10.4
#source = https://docs.python.org/3/library/sqlite3.html

import sqlite3 
con = sqlite3.Connection("users.db")#the sql connection

cur = con.cursor()# sql cursor 
def Create_connection(con_name):# ("exam.db")

    con = sqlite3.Connection(con_name)#the sql connection

    cur = con.cursor()# sql cursor 
def CreateTable(Ctable):
    #"CREATE TABLE movie(title, year, score)"
    cur.execute(Ctable)

    #select the names of the exist table 
    res = cur.execute("SELECT name FROM sqlite_master")

    print(res.fetchall())
  
def add_data(db_name,sql_command):
    con =sqlite3.connect(db_name)
    cur=con.cursor()
    cur.execute(sql_command)
    con.commit()

data = [
    (36, +972559329311,300257227),
    (28,+972542650209,308088582)
]
def Get_data():
    res = cur.execute("SELECT age FROM user")
    return res.fetchall()

    


