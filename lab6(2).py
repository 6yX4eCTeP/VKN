import math

a=float(input("a="))
b=float(input("b="))
h=float(input("h="))
x=a

while x<b:
    bar1= (math.cos(x)/(1+math.sin(x)))
    print (bar1)
    x = x+h
    if x>b:
        break
