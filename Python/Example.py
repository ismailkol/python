#Fig . 3.25: fig03_25.py
#using the break statement to avoidrepeating code
#in the class-average program.

total=0
gradecounter=0

while 1:
    grade=raw_input("Enter grade, 53 to end:")
    grade=int(grade)

    if grade ==53:
        break
    total+= grade
    gradecounter+=1

if gradecounter != 0:
    average =float(total)/ gradecounter
    print"Class average is", average
else:
    print"No grades were entered"
