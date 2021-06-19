#Fig. 2.19:fig002_pythonders.py
#String formatting.
integerValue =5361
print("integer" ,integerValue)
print("decimal integer %d" % integerValue)
print("hexadecimal integer %x\n" % integerValue)


floatValue =5361.5361
print("Float",floatValue)
print("Default float %f" %floatValue)
print("Default exponential %e\n"% floatValue)

print("Right justify integer (%8d)" %integerValue)
print("Left justify integer(%-8d)\n" % integerValue)

stringValue = "STRİNG FORMATTİNG"
print("Force eight digits in integer %.8d"% intergerValue)
print("Five digits after decimal in float %.5f" %floatvalue)
print("fifteen and five characters allowed in string:")
print("(%.15s) (%.5s)"% (stringvalue , stringvalue))
