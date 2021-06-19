import sqlite3

con=sqlite3.connect("derslerim.db")
cursor=con.cursor()


def degerAl():
    cursor.execute("Select * from tablo1")
    data=cursor.fetchall()



    for i in data:
        print("\n")
        for j in range(0,4):
         print(i[j])



    con.commit()
    con.close()

degerAl()