def sistem_bilgisi_göster():
    import sys
    print("\nSistemde kurulu Python'ın;")
    print("\tana sürüm numarası:", sys.version_info.major)
    print("\talt sürüm numarası:", sys.version_info.minor)
    print("\tminik sürüm numarası:", sys.version_info.micro)

    print("\nKullanılan işletim sisteminin;")
    print("\tadı:", sys.platform)

"""------------------------------------------------------------------------"""

def kare_bul():
    sayı = 12
    çıktı = "{} sayısının karesi {} sayısıdır"
    print(çıktı.format(sayı, sayı**2))
      


def F(x): #x(metinsel ifade) girdisi hazır.
    print(x,' Merhaba') 
    print(x, ' Naber')
    print(x, ' Nasılsın')
    # Burada gelen x girdilerine mesajlari veriyor.
 
 
F('Ali') # gelen 3 adet print komutunu ekrana yazdırıyor.
