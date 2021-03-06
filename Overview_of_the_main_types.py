'''
В данном разделе рассматриваются другие методы работы с типами данных, а также закрепляется изученный материал
'''
# В случае изменения объекта, ссылки на этот объект соответственно меняются
x = [1, 2, 3]
l = ['w', x, 'i']
d = {'X' : x, 'y' : 2}
print(l)
print(d)

x[1] = 'word'
print(l)
print(d)

# При создании копии объекта ссылка на элементы объекта отсутствует

a = [1, 2, 3]
b = {'q' : 1, 'w' : 2}
A = a[:]
B = b.copy()
A[1] = 4
B['e'] = 3
print(A)
print(a)
print(B)
print(b)

L1 = [1, [2, 3], 4]
L2 = [1, [2, 3], 4]
print(L1 == L2)    # Эквивалентный значения
print(L1 is L2)    # Ссылки на разные объекты

S1 = 'map'
S2 = 'map'
print(S1 == S2, S1 is S2)    # Значения коротких строк кэшируются. Не работает для длинных строк

D1 = {'a' : 1, 'b' : 2}
D2 = {'a' : 1, 'b' : 3}
#print(D1 < D2)    Данная операция невозможна, т.к. требует больших затрат

print(sorted(D1.items()) < sorted(D2.items()))    # Сравнение возможно при данном подходе

