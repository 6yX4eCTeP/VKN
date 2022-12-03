#2. Написати програму, яка виведе на екран вміст каталога Program Files і запише у файл w.txt назви всіх фйалів, які знаходяться у каталогу Windows (або інший, в якому встановлена операційна система). 
    
import os
 
pf = os.listdir(r'C:\Program Files')
print(pf)
 
windows = []
for f in os.listdir(r'C:\Windows'):
    if os.path.isfile(os.path.join(r'C:\Windows', f)):
        windows.append(f)
 
with open('w.txt', 'w') as f:
    f.write('\n'.join(windows))
