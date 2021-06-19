total=0
gradecounter= 0
grade= raw_input("Enter grade,-1 to end:")
grade=int(grade)

while grade != -1 :
    total=total + grade
    gradecounter=gradecounter +1
    grade=raw_input("Enter grade , -1 to end:")
    grade=int(grade)

if gradecounter != 0 :
    average=float(total)/ gradecounter
    print"class average is",average
else:
    print"No grades were entered"
