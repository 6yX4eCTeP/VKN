import math 
def func1(x1,y1,z1):
    b=(0.7*math.cos(x1))+math.log10(math.fabs(y1))**(1/5)
    a=(math.e)**(z1+x1)
    f=b+a
    return(f) 
x=float(input("Введіть х "))
y=float(input("Введіть y "))
z=float(input("Введіть z "))
f=func1(x,y,z)
print(f)
