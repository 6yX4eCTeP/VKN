#Текстові файли містить словники з роками випуску і цінами на мобільні телефони. Написати програму, яка виведе відомості про: 1) найновіші мобільні
# телефони; 2) 2-3 найдешевші моделі мобільних телефонів.
import json
 
with open('price.json', 'r', encoding='utf-8') as p:
    d = json.load(p)

    
d.get('phone', []).sort(key=lambda x: x.get('price', 0))

print(d.get('phone', [])[:2])
with open('Model.json', 'r', encoding='utf-8') as m:
    k = json.load(m)

newest = max(k.get('phone', []), key=lambda x: x.get('year', 0))
print(newest)