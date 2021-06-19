# -*- coding: cp1254 -*-

def kayit_olustur(isim1,soyisim1,isis1,sehir1):

    isim1    = "Fırat"
    soyisim1 = "Özgül"
    isis1   = "Ubuntu"
    sehir1   = "İstanbul"

    print("isim           : ", isim1)
    print("soyisim        : ", soyisim1)
    print("işletim sistemi: ", isis1)
    print("şehir          : ", sehir1)

    print("-"*30)

isim2    = "Mehmet"
soyisim2 = "Öztaban"
isis2   = "Debian"
sehir2   = "Ankara"

print("isim           : ", isim2)
print("soyisim        : ", soyisim2)
print("işletim sistemi: ", isis2)
print("şehir          : ", sehir2)

print("-"*30)


"""-----------------------------------------------------------------"""

def sistem_bilgisi_göster():
    import sys
    print("\nSistemde kurulu Python'ın;")
    print("\tana sürüm numarası:", sys.version_info.major)
    print("\talt sürüm numarası:", sys.version_info.minor)
    print("\tminik sürüm numarası:", sys.version_info.micro)

    print("\nKullanılan işletim sisteminin;")
    print("\tadı:", sys.platform)
