from day import dbconnection
import pymysql
con=pymysql.connect(user="root",password="",host="localhost",database="hospitaldb")
def insert(qry):
    cu=con.cursor()
    cu.execute(qry)
    con.commit()
def selectall(qry):
    cu=con.cursor()
    cu.execute(qry)
    data=cu.fetchall()
    return data
def delete(qry):
    cu=con.cursor()
    cu.execute(qry)
    con.commit()
def selectone(qry):
    cu=con.cursor()
    cu.execute(qry)
    data=cu.fetchone()
    return data
def update(qry):
    cu=con.cursor()
    cu.execute(qry)
    con.commit()