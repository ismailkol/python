faktoriyel=1

while True :
    sayı=int(input("Lütfen negatif olmayan bir sayı giriniz:"))
    if (sayı <0) :
          print("Lütfen negatif olmayan bir sayı giriniz!!!")



    else:
          for a in range(1,sayı+1):
             faktoriyel *= a


          print("faktoriyel",faktoriyel)
          break
