import sqlite3
import random
import time
import datetime


con = sqlite3.connect("derslerim.db")
cursor = con.cursor()


def tabloOlustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS tablo1(zaman REAL,tarih TEXT,anahtarkelime TEXT,deger REAL)")
    con.commit()

def rastgeleDegerEkleme():
    zaman=time.time() #şimdiki zamanı alrı
    tarih=str(datetime.datetime.fromtimestamp(zaman).strftime('%Y-%m-%d %H:%M:%S'))
    anahtarkelime="Python Sqliste3"
    deger=random.randrange(0,10)
    cursor.execute("INSERT INTO tablo1(zaman,tarih,anahtarkelime,deger) VALUES(?,?,?,?)",(zaman,tarih,anahtarkelime,deger))
    con.commit()

i=0
while(i<10):
    rastgeleDegerEkleme()
    time.sleep(1) #1 sn sistemi uyutur
    i+=1



tabloOlustur()
con.close()





