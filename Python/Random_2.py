import random

spam = {12345: 'Luggage Combination', 42: 'The Answer'}

print(spam[12345])
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(eggs == ham)

spam = {'name': 'Zophie', 'age': 7}
print(spam['name'])



birthdays = {'ENES': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True: 
    print("ENTER A NAME: (blanck to get out)")
    name= input()
    if name == '':
        break
    if name in birthdays: 
         print(birthdays[name] + ' is the birthday of ' + name) 
    
    
