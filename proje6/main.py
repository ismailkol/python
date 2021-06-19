class Dusman:


    def __init__(self,isim="hasan",kalanCan=61,saldırıGucu=12,mermiSayisi=2): #classımız oluşturulurken çağrılan fonksiyon ayrıyeten açağırmadan başta calıştı
        self.isim=isim
        self.kalanCan=kalanCan
        self.saldırıGucu=saldırıGucu
        self.mermiSayisi=mermiSayisi



    def printf(self):
        print("Basılıyor......")
        print("isim: ",self.isim,"kalanCan: ",self.kalanCan,"saldırıGucu: ",self.saldırıGucu,"mermiSayisi: ",self.mermiSayisi)



class Dusman2:

    isim=""
    kalanCan=0
    saldırıGucu=0
    mermiSayisi=0

    def __init__(self,isim,kalancan,saldırıGucu,mermiSayisi):
        self.isim=isim
        self.kalanCan=kalancan
        self.saldırıGucu=saldırıGucu
        self.mermiSayisi=mermiSayisi

    def printf(self):
        print("Basılıyor......")
        print("isim: ", self.isim, "kalanCan: ", self.kalanCan, "saldırıGucu: ", self.saldırıGucu, "mermiSayisi: ",self.mermiSayisi)



dusman1=Dusman("koloğlari",6000,1200,10000)
dusman1.printf()

dusman2=Dusman2("kesatogli",1000,50,61)
dusman2.printf()

dusman3=Dusman()
dusman3.printf()



