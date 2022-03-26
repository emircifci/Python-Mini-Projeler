#2000 ile 3200 arasında 7 ile tam bölünen 5in kat sayısı olmayan sayılar
list=[]
for i in range(2000,3200):
    if i%7==0 and i%5!=0:
        list.append(str(i))
print(list)                    