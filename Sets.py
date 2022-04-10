'''
Множества являются изменяемыми уникальными неупорядоченными коллекциями элементов
'''

first_set = set('qwerty1234')    # Создание множества
second_set = set('wear532')
print(first_set | second_set)    # Конкатенация множеств

print(first_set & second_set)    # Пересечения множеств

print (first_set - second_set)     # Разница множеств

print(second_set - first_set)

first_list = [1, 2, 6, 7, 6, 2, 5]    # Удаление дублирующих элементов из списка
print(list(set(first_list)))

