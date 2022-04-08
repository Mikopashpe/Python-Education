'''
В данном разделе рассматриваются списки как один из типов упорядоченных объектов произвольных типов. 
Списки являются изменяемыми, что можно выделить как хороший инструмент для работы с данными.
'''

first_list = ['qwerty', 1234, 1.44, 'mu1']

print(len(first_list))    # Длина последовательности выводит не общее количество символов, а количество элементов списка

print(first_list[0], first_list[::-3])    # Слайсирование списка

print(first_list + [14, 'hh'])    # Конкатенация элементов в конец списка

first_list.append('oo')    # Добавление элемента в конец списка
print(first_list)

first_list.pop(4)
print(first_list)

first_list.insert(2, 'hh')    # Добавление элемента по индексу
print(first_list)

first_list.pop(2)    # Удаление элемента по индексу
print(first_list)

#first_list.sort()    # Сортировка списка невозможна, т.к. внутри списка содержатся разные типы данных
print(first_list)

first_list.reverse()    # Список в обратном порядке
print(first_list)

second_list = [[1, 2, 3, 4], [11, 22, 33, 44], [111, 222, 333, 444]]    # Пример вложенного списка

third_list = [i[3] for i in second_list]    # Списковое включение
print(third_list)

third_list = [i[1] + 1 for i in second_list]
print(third_list)

third_list = [i[1] for i in second_list if i[1] % 2 == 0]
print(third_list)

forth_list = list(range(8))
print(forth_list)

forth_list = (sum(i) for i in second_list)
print(forth_list)
print(next(forth_list), next(forth_list), next(forth_list))