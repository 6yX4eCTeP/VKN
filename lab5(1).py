import math
x=float(input("задайте х: ")) 
def fun1 (x):
    bar1= math.log1p(math.fabs(x-1))+ math.log10(math.fabs(pow(x,0.7)+2))
    return (bar1)
def fun2(x):
    bar2=math.e*4*pow(x,7)+2-pow(x,1/3)
    return (bar2)
def fun3 (x):
    bar3=4.27*x+4.33*pow(x,2)+math.sin(x+1)
    return (bar3)

if x>12.1:   
    print(fun1(x))

elif x>=-5.7 and x<=12.1:
   print(fun2(x))
elif x<5.7:
    print(fun3(x))
else:
    print("неправильно")
