note=float(input("Notunuzu giriniz:"))

if note >= 90 :
    print("AA aldınız.")
elif note > 80 :
    print("AB aldınız.")
elif note > 70 :
    print("BB aldınız.")
elif note > 60 :
    print("BC aldınız.")
elif note > 50 :
    print("CC aldınız.")
elif note > 45 :
    print("CD aldınız.")
else:
    print("Dersden başarısınız oldunuz.")

butSorusu= input("Bütünleme sınavına girecekmısınız?")

if butSorusu == 'evet' :
    print("Öğrenci işlerine başvurunuz.")
if butSorusu == 'hayır' :
    print("Eğitim hayatınızda başarılar dileriz.")
if butSorusu == ' ' :
    print("Soruyu cevaplamadınız sistemden atılacaksınız.\n Tekrar giriş yapınız.")

      
