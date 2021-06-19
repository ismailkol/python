defkullanıcı= "EnesKARAL"
defparola="trabzonrize6153"


while (True) :
    kullanıcı=input("Kullanıcı Adı:")
    parola=input("Parola:")
    if ((kullanıcı==defkullanıcı) and (parola==defparola)):
        print("hosgeldıniz",kullanıcı)
        break
    elif((kullanıcı!=defkullanıcı) and (parola==defparola)):
        print("Kulanıcı adını yanlış girdiniz!)

    elif((kullanıcı==defkullanıcı) and (parola!=defparola)):
              print("Şifrenizi mi unuttunuz?")
              print("Şifrenizi değiştirmek istermisiniz?(Evet/Hayır)")
              cevap=input()
              if (cevap == "Evet"):


                  yeniparola=input("Yeni parola:)
                  print("Lütfen bekleyiniz...")
                  defparola=yeniparola
                  print("Şifreniz başarıyla değiştirilmiştir...")

    else:
              print("Tekrar deneyiniz...")
