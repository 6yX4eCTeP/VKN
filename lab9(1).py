#Кортеж  містить дані кількох  типів:
#  рядки, дійсні і  цілі  числа, списки. Програма повинна записати списки в один вкладений список.
T = (123, 'qwe', None, 1.23, (123,), ['qwe', 123], [345], ['asd'])
a = [x for x in T if isinstance(x, list)]
print(a)