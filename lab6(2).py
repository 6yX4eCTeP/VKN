import math

a=int(input("a="))
b=int(input("b="))
h=int(input("h="))
x=a
spisok = []
while x<b:
    spisok.append(math.cos(x)/1+math.sin(x))
    x += h
    if x>b:
        break
print (spisok)