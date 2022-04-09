'''
В данном разделе приведены примеры работы со словарями: вариации создания словаря, изменение значения ключа, добавление ключа и значения и др. 
'''

first_dict = {'liquid' : 'Cocacola', 'color' : 'darkbrown', 'quantity': 4}    # Создание словаря

print(first_dict['liquid'])

first_dict['quantity'] += 2    # Изменение значения вызовом по ключу
print(first_dict)

second_dict = {}    # Второй метод создания словаря
second_dict['name'] = 'Johnn'
second_dict['age'] = 40
second_dict['Job'] = 'teacher'
print(second_dict)

Teacher1 = dict(name = 'Johnn', age = 40, Job = 'teacher')    # Третий метод создания словаря
print(Teacher1)

Teacher2 = dict(zip(['name', 'job', 'age'], ['Johnn', 'teacher', 40]))    # Четвертый метод создания словаря
print(Teacher2)

Third_dict = {'name' : {'first_name' : 'Bill', 'last_name' : 'Blake'}, 'jobs' : {'writer', 'doctor'}, 'age' : 42.3}    # Создание вложенного словаря
print(Third_dict['name']['last_name'])

Third_dict['jobs'].add('journalist')     # Добавление дополнительного значения в словарь
print(Third_dict['jobs'])

Third_dict['drivers_license'] = 'yes'    # Способ добавления пары ключ : значение
print(Third_dict)

if not 'Diploms' in Third_dict:    # Поиск ключа через условие
    print('absent\nbut you can create this key')

age_value = Third_dict.get('age')    # Поиск значения по ключу с помощью .get
print(age_value, Third_dict['age'])

D = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4}
K = list(D.keys())    # Создание нового списка из ключей словаря
K.sort()    # Сортировка списка
print(K)

for key in K:    # Итерация ключей из списка
    print(key, '=>', D[key])

b = [x * 2 for x in D.values()]    # Изменение значений 
print(b)