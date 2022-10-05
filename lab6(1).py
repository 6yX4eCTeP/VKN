import math
a=float(input("a="))
b=float(input("b="))
h=float(input("h="))
x=a
for x in range(1, 100):
    bar1=math.cos(x)/(1+math.sin(x))
    print(bar1)
    if x == b:  
         break
