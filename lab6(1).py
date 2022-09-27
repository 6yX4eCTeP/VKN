import math
a=int(input("a="))
b=int(input("b="))
h=int(input("h="))
x=a
for x in range(1, 100):
    bar1=math.cos(x)/1+math.sin(x)
    print(bar1)
    if x == b:  
         break
