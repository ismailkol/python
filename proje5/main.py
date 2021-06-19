import sqlite3
import random

con=sqlite3.connect("derslerim.db")

cursor=con.cursor()



def veriGüncelleme():

    print("Güncellenmemiş veri: \n")
    cursor.execute("Select * from tablo1")
    data=cursor.fetchall()

    for i in data:
        print(i)

    sayi=9

    orn=50
    ornStr=str(orn)
    print(ornStr+"\n")
    print("Güncellenmiş  veri: \n")
    cursor.execute("UPDATE tablo1 SET deger = 15 where deger=6")
    cursor.execute("Select * from tablo1")
    data = cursor.fetchall()
    for i in data:
        print(i)
    con.commit()
    con.close()

veriGüncelleme()

