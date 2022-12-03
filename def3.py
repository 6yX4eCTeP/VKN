import math
class Student:
    SName= ''
    Year = 0
    Marks= []
    AverMark= 0.0
    def __init__(self,SName,Year, Marks):
        self.SName=SName
        self.Year=Year
        self.Marks=Marks  
    def CalcAvMark (self,Marks):   
        self.AverMark= math.fsum(Marks) / len(Marks)
        
        
    def displayALL(self):  
         print('Модель: {}. Рік народження: {}. Список оцінок: {}. Середнє: {}'.format(self.SName, self.Year, self.Marks,self.AverMark))
    def  displayST(self):
        if self.AverMark>= 4.5:
           print('Модель: {}. Рік народження: {}. Список оцінок: {}. Середнє: {}'.format(self.SName, self.Year, self.Marks,self.AverMark)) 



    