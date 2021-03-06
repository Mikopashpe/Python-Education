'''
В данном разделе рассматриваются более глубокие методы работы с типом данных кортеж.
'''


a = (1, 2)
b = (3, 4)
c = a + b    # Конкатенация кортежей
print(c)

c = b*4    # Повторение
print(c)

print(c[1], c[0:5])    # Поиск по индексу и слайсирование

t = list(c)    # Создание списка из кортежа
t.sort()    # Сортировка списка
c = tuple(t)    # Создание кортежа из сортированного списка
print(c)
print(c.count(4))    # Счетчик количества передаваемых элементов

q = (1, [2, 3], 4)
q[1][1] = 'liquid'    # Можно изменить изменяемые объекты внутри кортежа
print(q)

e = ('a', 'b', 'c')
first, second, third = e   # Присваивание кортежей
print(first, second, third)