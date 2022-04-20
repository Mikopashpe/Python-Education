'''

'''

a = list(range(0, 10, 2))   # Range создает физический итерируемый список
print(a)

for i in range(4):    # Функция может повторять действин необходимое количество раз в цикле for
    print(i, 'times')


'''x = 'word'
for i in x:
    print(i, end = ' ')

y = 0
while y < len(x):
    print(x[y], end = ' ')
    y += 1'''


'''m = 'robot'
for i in range(len(m)):    # Ручная итерация
    print(m[i], end = ' ')'''


a = 'drbujvj'
for i in range(len(a)):
    a = a[i:] + a[:i]
    print(a)


l = [1, 2, 3, 4]
for i in range(len(l)):
    l[i] += 1
print(l)


l2 = [5, 6, 7, 8]
for (x, y) in zip(l, l2):
    print(x, y)