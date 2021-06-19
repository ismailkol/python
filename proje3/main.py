import urllib.request
import urllib.parse

#siteAdresi="https://www.google.com.tr"
#siteAdresi=input("hangi siteye girmek istersiniz ?")
#siteye baglanıp kaynak kodunu çektik

#html=urllib.request.urlopen(siteAdresi)

#kaynak kodunun okuyarak ekrana yazdırdık

#print("\n\nistediginiz sitenin kaynak kodu\n\n")
#print(html.read())

# siteye veri gönderme

site_adresi="http://google.com/"

veriler={
    "kullaniciAdi":"mustafa",
    "sifre":"123456",
    "eMail":"msutafa@aydemir.im",
    "isim":"mustafa aydemir"

}
#siteye gönderilecek veriler özel karakterleri şifreledik
parametreler=urllib.parse.urlencode(veriler)




#sitenin tam halini olusturduk
tam_Site_Adı=site_adresi+"?"+  parametreler




#istegimiz gönderdik
html=urllib.request.urlopen(tam_Site_Adı)

print("\nistedigimiz sitenin bilgilerndirici metin yazdık\n")
print(html.read())

