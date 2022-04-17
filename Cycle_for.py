'''
В данном разделе изучаются основы работы цикла for
'''

sum = 0

for x in [1, 2, 3, 4, 5]:
    sum = sum + x    # В данном примере выводится сумма итерации
print(sum)

String_ex = 'kjbjkskjpowf'
Tuple_ex = (12, 34, 56, 78, 90)

for x in String_ex:    # Цикл работает со строками
    print(x, end = ' ')

for x in Tuple_ex:    # Цикл также работает с кортежами
    x *= 2
    print(x, end = ' ') 


new_dict = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}

for (key, value) in new_dict.items():    # Цикл работает со словарями по ключам и значениям
    print(key, '=', value)

String_ex2 = 'kgfskbfoiwwdbiyqwyg'
srtlist = []

for x in String_ex:
    if x in String_ex2:
        srtlist.append(x)    # Результат отработки цикла на общие элементы записывается в пустой список
print(srtlist)