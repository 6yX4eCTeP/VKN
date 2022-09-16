import math 
x=float(input("Введіть х "))
y=float(input("Введіть y "))
z=float(input("Введіть z "))
b=(0.7*math.cos(x))+math.log10(math.fabs(y))**(1/5)
a=(math.e)**(z+x)
f=b+a
print(f)
