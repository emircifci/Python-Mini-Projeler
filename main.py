def merhabakullanici():
    isim = input("kullanıcı adınız ")
    print("Merhaba {}".format(isim))
def ikiSayiToplama():
    s1 = int(input("1. sayıyı giriniz"))
    s2 = int(input("2. sayıyı giriniz"))
    print (s1+s2 )
def ortalamaHesaplama():
    vize = int(input("vize notu giriniz ; "))
    final = int(input("final notu giriniz ; "))
    Ortalama =(vize*0.3)+(final*0.7)
    print("Ortalamanız : {}".format(Ortalama))
def sinifGecildimi():
    ortalama = int(input("ortalama notu giriniz ; "))
    if ortalama>=50 :
        print("tebrikler geçtiniz")
    else:
        print("malesef kaldınız")           
def SayiTekMiCiftMi():
    s3 = int(input("Merak etiğiniz sayıyı giriniz ; "))
    if s3%2==0:
        print ("sayi çift")
    else:
        print("sayi tekdir")
def ilkYuzSayi():
    for i in range(101):
        print(i)
def ilkYuzSayi2():
    for i in range(0,101,2):
        print(i)
def metinYazdirma():
    metin =input("metni giriniz")
    for h in metin:
        print(h)
def ikisayininarasindakisayilar():
    s1 = int(input("1. sayıyı giriniz"))
    s2 = int(input("2. sayıyı giriniz"))
    toplam=0
    for i in range(s1+1,s2):
        toplam = i+toplam
    print(toplam)
def sayiAsalMi():
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
from math import factorial
from random import randint
def sayiTahmin():    
    rand=randint(1, 100)
    sayac=0
    
    while True:
        sayac+=1
        sayi=int(input("1 ile 100 arasında değer girin (0 çıkış):"))
        if(sayi==0):
            print("Oyunu İptal Ettiniz")
            break
        elif sayi < rand:
            print("Daha Yüksek Bir Sayı Girin.")
            continue
        elif sayi > rand:
            print("Daha Düşük Bir Sayı Girin.")
            continue
        else:
            print("Rastele seçilen sayı {0}!".format(rand))
            print("Tahmin sayınız {0}".format(sayac))   
def yuzyashesaplama():
    isim = input("kullanıcı adı giriniz ; ")
    yas =int(input("yaşınızı girinizi"))
    yuzyas = (2020-yas )+100
    print("Merhaba {}  100. yaşınıza  {} yılında giriceksiniz ".format(isim , yuzyas))
def program1():
#2000 ile 3200 arasında 7 ile tam bölünen 5in kat sayısı olmayan sayılar
    list=[]
    for i in range(2000,3200):
        if i%7==0 and i%5!=0:
            list.append(str(i))
    print(list)                    
def faktoriyel():
    sonuc=1
    s1 = int(input())
    for i in range (1,s1+1):
        sonuc=sonuc*i
    print(sonuc)    

