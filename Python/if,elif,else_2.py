defkullanıcı="abc"
defparola="xyz"

kullanıcı=input("kullanıcı adı:")
parola=input("parolanuz:")


if((defkullanıcı==kullanıcı) and (defparola==parola)):
    print("Hoşgeldiniz")
elif((defkullanıcı!=kullanıcı) and (defparola==parola)):
   print("Kullanıcı adı yanlış")
elif((defkullanıcı==kullanıcı) and (defparola!=parola)):
    print("Şifreniz yanlıştır")
else:
    print("Lütfen tekrar deneyiniz...")
                  
