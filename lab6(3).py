import math
a = float(input('Задайте a'))
b = float(input('Задайте b'))
h = float(input('Задайте h'))
x = a
spisok = []
while x<b:
    spisok.append(math.cos(x)/1+math.sin(x))
    x += h
    if x>b:
        break
Foo1 = 0
while Foo1 != len(spisok):
    print(spisok[Foo1])
    Foo1 += 1
spisok.sort()
spisok.pop(0)
spisok.pop(-1)
print(spisok)
