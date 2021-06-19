"""DERS-STRINGLERDE LEN VE GRUPLAMA"""

"""BİR ornekle bu konuyu anlatmak ıstıyorum..."""

x="PYTHON PROGRAMLAMA HOS GELDINIZ"
"""  x="PYTHON PROGRAMLAMA HOS GELDINIZ"
    [0 1 2 3 ... 30 31] soldan saga dogru sıralmadır.
    [-32 -31 ... -2 -1] sagdan sola dogru sıralamadır."""

print(x)

print(x[0])
print(x[1])
print(x[2])
print(x[3])
"""bu soldan saga dogru sıralamanın gruplamasıdır"""
print(x[-1])
print(x[-2])
print(x[-3])
print(x[-4])
"""bu sagdan sola dogru sıralamanın gruplamasıdır"""
print(x[2:7])
print(x[:7])
print(x[3:])
print(x[ : ])
""" burda ılk yazılandan son yazılana kadardır bunun ıcın son yazılan deger kayıt alınmaz
Bos bırakılan taraf ıse baslangıc yada son demektır."""

print(len(x))
"""Bu durum ıse yazılan strıngın uzunlugunu bıze vermektedır."""
