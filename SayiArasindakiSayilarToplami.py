s1 = int(input("1. sayıyı giriniz"))
s2 = int(input("2. sayıyı giriniz"))
toplam = 0
for i in range(s1+1, s2):
    toplam = i+toplam
print(toplam)
