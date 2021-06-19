ktunote=float(input("Notunuzu giriniz:"))

if ktunote >= 90 :
    print("AA aldınız.")
elif ktunote > 80 :
    print("AB aldınız.")
elif ktunote > 70 :
    print("BB aldınız.")
elif ktunote > 60 :
    print("BC aldınız.")
elif ktunote > 50 :
    print("CC aldınız.")
elif ktunote > 45 :
    print("CD aldınız.")
else:
    print("Dersden başarısınız oldunuz.")

butsorusu= input("Bütünleme sınavına girecekmısınız?")

if butsorusu == 'evet' :
    print("Öğrenci işlerine başvurunuz.")
if butsorusu == 'hayır' :
    print("Eğitim hayatınızda başarılar dileriz.")
if butsorusu == ' ' :
    print("Soruyu cevaplamadınız sistemden atılacaksınız.\n Tekrar giriş yapınız.")

      
