#Список  налічує  9  об´єктів  класу  COMP  (комп´ютер).  Клас COMP  має такі властивості: модель, інвентарний номер, ціна.
#  Клас СОМР має такі методи: конструктор класу, деструктор класу, зміна інвернатрного номера, зміна ціни.
# Програма  повинна виконувати  операції  як  з  список,  так і  з  кожним окремим об´єктом. 

class COMP ():
    
    nv_numb= ''
    model=''
    price = 0.0
    """Опис"""
    def __init__ ( self ,nv_numb, model, price  ):
        """Атрибути"""
        self.nv_numb = nv_numb
        self.model = model
        self.price = price
    def read_price(self):
            print('Ціна: {}.'.format(self.price))
    def update_price ( self , new_price):
        """Встановлює нове значення ціни"""
        self.price = new_price

    def read_nv_numb(self):
            print('Інвентарний номер: {}.'.format(self.nv_numb))
    def update_nv_numb ( self , new_nv_numb):
        """Установлює нове значення інвентарному номеру"""
        self.nv_numb = new_nv_numb
    
    def get_full_name(self):  
        print('Оновнений номер: {}. Модель: {}. Оновлена ціна: {}'.format(self.nv_numb, self.model, self.price))
    #def __del__(self):
    #    print('Видалимо усе '+self.__str__())
    
comp_2 = COMP('19429491', 'a4', 10000)
comp_1= COMP('194292191', 'a3', 6000)

list1=[comp_1, comp_2]
list=[]
list2=[]
L=len(list1)
#Виконуємо операції зі списком
def function1(list, L):
    for i in range (L):
        k=list1[i]. read_price(),list1[i]. update_price (17100), list1[i]. read_price()
        list.append(k)
    return(list)
def function2(list2, L):
    for o in range (L):
        k1=list1[o]. read_nv_numb(),list1[o]. update_nv_numb (4214554), list1[o]. read_nv_numb()
        list2.append(k1)
    return(list2)
#function1(list, L)
#function2(list2, L)

k3= comp_2. read_price(), comp_2. update_price (12), comp_2. read_price()
list1.append(k3)
k4= comp_1. read_price(), comp_1. update_price (12.1), comp_1. read_price()
list1.append(k4)
k31= comp_2. read_nv_numb(), comp_2. update_nv_numb (13), comp_2. read_nv_numb()
list1.append(k31)
k41= comp_1. read_nv_numb(), comp_1. update_nv_numb (13.1), comp_1. read_nv_numb()
list1.append(k41)
a=comp_2.get_full_name()
b=comp_1.get_full_name()

