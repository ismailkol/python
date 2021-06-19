#Fig 2.25: fig02_25 python ders
#using if statements, relational operators and equality
#operators to show improper indentation

print("Enter two integers, and I will tell you")
print("the relationships they satisfy")


"""read first string and convert to integer"""
number1 =raw_input("Please enter first integer:") 
number1=int(number1)
"""read second string and convert to integer"""
number2=raw_input("Please enter second integer:")
number2=int(number2)

if number1==number2 :
  print("%d is equal to %d") %(number1,number2)
if number1!= number2 :
  print("%d is not equal to %d") %(number1,number2)
if number1 < number2 :
  print("%d is less than %d ") % (number1,number2)
if number1 > number2 :
  print("%d is greater than %d") % (number1,number2)
if number1 <= number2 :
  print("%d is less than or equal to %d") %(number1,number2)
if number1 >= number2 :
  print("%d is greater than or is equal to %d") % (number1,number2)

