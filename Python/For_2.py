#Fig. 3.23:fig03_23.
#calculating compound interest(bırlesık faız hesaplama)

principal=20000
rate=.05

print"Year %21s" % "Amount on deposit"
for year in range(1,61):
    amount =principal *( 1.0 + rate)** year
    print"%4d%21.2f" % (year , amount)
