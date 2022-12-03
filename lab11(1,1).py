#Написати програму, яка запишу у файл дані про роки народження 10-15 письменників у порядку зростання. Прізвища і роки задаються користувачем

import csv
import sys
a=str(input("1"))
b=str(input("2"))
c=str(input("3"))
#bar1=str(input("4"))
#bar2=str(input("5"))
#bar3=str(input("6"))
#bar4=str(input("7"))
#bar5=str(input("8"))
#bar6=str(input("9"))
#bar7=str(input("10"))
#,bar1:4, bar2:5, bar3:6, bar4:7, bar5:8,bar6:9,bar7:10
D={a:1, b:2,c:3}

D1 = {}
for key in D:
    D1[key]=int(input(""))
print (D1)
sort_D1={}
sort1=sorted(D1,key=D1.get)

for i in sort1:
    sort_D1[i]=D1[i]
print (sort_D1)
a=[sort_D1]
with open('gogs.csv', 'w', newline='') as f: 
    fieldnames=a[0]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(sort_D1)

    