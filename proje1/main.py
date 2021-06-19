with open("deneme.txt","r+") as dosya:
   data=dosya.readlines()
   data.insert(1,"fatih kol")
   dosya.seek(0)
   dosya.writelines(data)








