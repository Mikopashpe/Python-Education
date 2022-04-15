'''

'''

a = [1, 2, 3, 4]
b = '56'
print(a + list(b))    # Для операций со строками и списками необходимо привести их к одному типу
print(b + str(a))

print(a[:1], a[:2], a[-1], a[-4])    # Нарезание списка

new_list = [[1, 2, 3], [11, 22, 33], [111, 222, 333]]
print(new_list[1], new_list[2][1])    # Поиск элемента по позиции в списке

new_list[1] = 'word'    # Изменение значения в списке по позиции
print(new_list)

new_list[0][0:2] = [15]    # Замена элемента во вложенном списке
print(new_list)

new_list.extend(['doom', 43, 54])    # Расширение списка. Элементы добавляются в конец списка
print(new_list)

new_list.append([90, 25])    # Расширение списка. Элементы добавляются в конец списка
print(new_list)

second_list = [1, 2]
second_list.extend([3, 4, 5])
print(second_list)

second_list.pop()    # Удаление последнего элемента в списке
print(second_list)

second_list.reverse()    # Изменение порядка списка
print(second_list)

second_list =list(reversed(second_list))    # Еще один способ изменения порядка в списке
print(second_list)

print(second_list.index(2))    # Получение индекса элемента

second_list.insert(2, 15)    # Добавление элемента по индексу
print(second_list)

second_list.remove(15)    # Удаление указанного элемента
print(second_list)

second_list.pop(2)    # Удаление элемента по индексу
print(second_list)

print(second_list.count(4))    # Счетчик элементов

del new_list[2:]    # Удаление среза
print(new_list)

first_dict = {'first_word' : 1, 'second_word' : 2, 'third_word' : 3}    # Создание словаря
print(first_dict)
print(first_dict['first_word'])    # Запрос значения по ключу
print(len(first_dict))    # Запрос длины словаря

first_dict['second_word'] = ['one', 'two']    # Изменение словаря путем присваивания вложенного списка ключу
print(first_dict)

first_dict['new_key'] = 'new_value'    # Присваивание значения по ключу
print(first_dict)

del first_dict['second_word']    # Удаление ключа
print(first_dict)

print(list(first_dict.values()))    # Вывод значений словаря
print(list(first_dict.keys()))    # Вывод ключей словаря

second_dict = {'second_word' : 2}
first_dict.update(second_dict)    # Объединение словарей
print(first_dict)

A = {'name' : 'Kate', 'age' : 28}    # Традиционное литеральное выражение
print(A)

B = {}    # Динамическок присваивание по ключам
B['name'] = 'Helen'
B['age'] = 30
print(B)

C = dict(name = 'Bob', age = 41)    # Форма dict с ключевыми аргументами
print(C)

D = dict([('name', 'Johnn'), ('age', 35)])    # Форма dict с кортежами "ключ/значение"
print(D)

ex_dict = dict.fromkeys(['a', 'b', 'c'], 0)    # Метод создания словаря с помощью .fromkeys
print(ex_dict)

keylist = ['apple', 'hp', 'samsung']
valuelist = ['ios', 'windows', 'android']
new_dict = dict(zip(keylist, valuelist))    # Создание словаря с помощью zip и списков
print(new_dict)

d = {x: x**3 for x in range(1, 6)}    # Создание словаря при помощи цикла
print(d)

c = dict.fromkeys('jazz')    # Метод .fromkeys создания словаря
print(c)
