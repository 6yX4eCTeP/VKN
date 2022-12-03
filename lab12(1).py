#Користувач задає рядок символів. Програма повинна:
#  1) дописати після кожного слова додаткові пробіли (до тих пір, поки довжина рядка не стане кратною 4) і вивести рядок на екран по 4 символи у рядку;
#  2) вивести перше і останнє слова рядка. Для цього розробити 2 функції.
a=str(input('a='))
b=a.split()
print(b)
k8=[]
L=len(b)
def function1(k8, L):
    for i in range (L):
        k1=str(b[i].ljust(4,' '))
        k8.append(k1)
    print(k8)

def function2(k8, L):
    print(k8[1],k8[2])
function1(k8, L)
function2(k8, L)

#if len(k)//4:
#    print('ok')
#else:
#    print('False')

