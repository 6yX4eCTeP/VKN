#Написати  модуль,  що  міститиме  опис  класу  STUDENT  з  такими властивостями:
#Name, SName (ім´я та прізвище), Year (рік народження), Marks (список оцінок), AverMark (середня оцінка).
#Написати для класу STUDENT такі методи:  конструктор  класу,  CalcAvMark  (обчислення  середньої  оцінки), DisplayAll (виводить всі відомості про студента).
# В основні програмі створити список  студентів  підгрупи  (10-12  елементів),
#вивести  відомості  про  тих студентів, які отримують стипендцію (середня оцінка має бути більшою за 4,5). Варіант 16 
import def3

student1= def3.Student( 'Іванов', 17, [5,5,5,4,5] ) 
k=student1.CalcAvMark([5,5,5,4,5])

student2= def3.Student( 'Тіхонов', 17, [4,5,3.5,5,5] ) 
k1=student2.CalcAvMark([4,5,3.5,5,5])

student3= def3.Student( 'Іванов', 17, [5,5,5,4,5] ) 
k2=student3.CalcAvMark([5,5,5,4,5])

student4= def3.Student( 'Іванов', 17, [5,3,5,4,3] ) 
k3=student4.CalcAvMark([5,3,5,4,3])


#student5= def3.Student( 'Іванов', 17, [5,3,3,4,5] ) 
#k4=student1.CalcAvMark([5,5,5,4,5])

#student6= def3.Student( 'Тіхонов', 17, [5,3,3,4,5] ) 
#k5=student6.CalcAvMark([4,5,3.5,5,5])

#student7= def3.Student( 'Іванов', 17, [5,3,3,4,5] ) 
#k6=student7.CalcAvMark([5,5,5,4,5])

#student8= def3.Student( 'Іванов', 17, [5,3,3,4,5] ) 
#k7=student8.CalcAvMark([5,3,5,4,3])
student1.displayST()  
student2.displayST() 
student3.displayST() 
student4.displayST() 

    



