#Написати модуль, який міститиме такі функції: 1) для обчислення суми N  перших  членів  геометричної  прогресії;
#  2)  для  обчислення  N-го  члена геометричної прогресії.
#  Підключити модуль до основної програми і виконати відповідні обчислення.
# Запросим ввод параметров прогрессии с клавиатуры 
n1 = int(input('Введите число элементов прогрессии: '))
b_first1 = int(input('Введите первый элемент прогрессии: '))
q1 = int(input('Введите знаменатель прогрессии: '))
 
print(b_first1)
def summa(b_first,q,n):
    b_prev = b_first
 
    summa = b_prev
    for i in range(1,n):
        b_cur = b_prev*q
        print(b_cur)
     
        summa = summa+b_cur
        b_prev = b_cur 
    return(summa)
print(summa(b_first1,q1,n1)) 


