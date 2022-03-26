sonuc = False
s1 = int(input("1. sayıyı giriniz"))
for i in range (2,s1):      
    if s1%i==0:
        sonuc = True
        break
if sonuc==True:
    print("asal değil")
else:
    print("asal")