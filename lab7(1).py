import re
s=input("Введіть рядок:")
print(re.sub(r'(?<=\d).+(?=\d)', ' ', s))
