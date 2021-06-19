import urllib.request
import re

try:
    #site adresini kullanıcıdan istedik
    siteAdresi=input("Sitenin adını girin: ")
    print("\n")
    #siteye baglanıp html kodunu aldık
    html=urllib.request.urlopen(siteAdresi)
    html=html.read()
    html=str(html)
    print(html)
    print("\n\n")

    #REGEX ile istegimiz etiketin tanımını yaptık
    tanim= "<head>(.*?)</head>"

    #REGEX ile istedigiz kaynak kodların icerisinde arıyoruz
    ara=re.search(tanim,html)

    #REGEX ile istedigiz kaynak kodların icerisinde arıyoruz
    if ara:
        etiket=ara.group(0) #istedigimzi etiketi html kodu ile birlikte getirdik

        icerik=ara.group(1) #istedigimiz etikeri sadece içerigi getirdik
        print("Etiket: "+etiket)
        print("icerik: "+icerik)
    else:
        print("istedigimiz etiket kaynak kodlari icerisnde bulunmamaktadir")

except:
    print("beklenmeyen bir hata oldu")

