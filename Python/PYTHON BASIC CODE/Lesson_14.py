defkullanıcı="abc"
defparalo="xyz"

kullanıcı = input("kullanıcı adınızı giriniz:")
paralo =input("paralonızı giriniz:")

if ((defparalo==paralo) and (defkullanıcı==kullanıcı)):
    print("sisteme hoşgeldiniz.")
elif((defparalo==paralo) and (defkullanıcı!=kullanıcı)):
     print("kullanıcı adınızı yanlış girdiniz!")
elif((defparalo !=paralo) and (defkullanıcı==kullanıcı)):
     print("paralonuzu yanlıs gırdınız!")
else:
     print("Hatalı giriş.")
