'''

'''

def times(x, y):    # Простой пример создания функции
    return x * y
print(times(2, 4))


l1 = [12, 23, 34, 45]
l2 = [34, 45, 56, 67]

def intersection(l1, l2):
    res = []
    for i in l1:    # Функция может содержать цикл. Цикл может содержать функцию
        if i in l2:
            res.append(i)
    return res
print(intersection(l1, l2))

s1 = 'spam'     # Функция может работать с разными типами данных
s2 = 'scam'
print(intersection(s1, s2))

x = intersection([1, 2, 3, 4, 5], (2, 4, 3, 7, 5))    # Пример работы функции с разными типами данных в качестве аргументов
print(x)

