'''
В данном разделе рассматриваются списки как один из типов упорядоченных объектов произвольных типов. 
Списки являются изменяемыми, что можно выделить как хороший инструмент для работы с данными.
'''

first_list = ['qwerty', 1234, 1.44, 'mu1']

print(len(first_list))    # Длина последовательности выводит не общее количество символов, а количество элементов списка

print(first_list[0], first_list[::-3])

print(first_list + [14, 'hh'])

first_list.append('oo')
print(first_list)

first_list.pop(4)
print(first_list)

first_list.insert(2, 'hh')
print(first_list)
