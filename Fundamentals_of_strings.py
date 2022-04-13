'''
В данном разделе идет углубленная работа со строковым типом данных.
'''

from dataclasses import replace


a, b = 'apple', "apple"    # Нет разницы при использовании двойныйх и одинарных кавычек
print(a == b)

a, b = 'knight\'s', "knight\"s"    #  Использование экранирования
print(a, b)

s = 'some\n\tbod\n\t\ty'    # Применение символов новой строки и табуляции
print(s)
print(len(s))    

s = 'C\\p\\m'    # При выводе сохраняется только один символ "\"
print(s)

S = 'Spam'
print(S[0], S[-3], S[2], S[-1])    # Вывод результата индексации строки
print(S[0] == S[-4])    # Пример использования прямой и обратной индексации
print(S[0:3])    # Срез строки по индексам
print(S[::1])    # Срез строки с шагом 1
print(S[::-1])    # Срез строки в обратном порядке

x = 44
y = '44'
print(x + int(y))    # Перевод строки в число, сложение
print(y + str(x))    # ПЕревод числа в строку, конкатенация

s = 'Nein!'
s = s + 'Mein'
print(s)    # Создание нового объекта
s = s[:4] + 'Auf' + s[-5]
print(s)    # Создание нового объекта со срезом

e = 'cameltown'
e = e.replace('ltown', 'rton')
print(e)    # Создание нового объекта заменой части

t = 'This is %d %s texts' % (1, 'of')
print(t)

w = 'This is {0} {1} texts'.format(1, 'of')    # Форматирование с помощью format()
print(w)

r = s.find('ei')    # Поиск внутри объекта. Возвращается место по индексу, где был расположен элемент
print(r)

longword = 'itegbtyuXXXXiwetryhiwtXXXXiuryewityihiXXXX'
longword = longword.replace('XXXX', 'YYY', 2)    # Замена части строки с учетом указанного количества замен
print(longword)

L = list(longword)
print(L)    # Преобразование строки в список

L[12] = 'bbbbbb'
L[2] = 'FRFRRFR'
print(L)    # Замена элементов в списке по индексу

longword = ''.join(L)    # Преобразование списка в строку методом ''.join()
print(longword)

print(longword.split('i'))    # Разделение строки по указанному значению

animal_dict = {'animal' : 'cat', 'count' : 1}
Line = 'i have %(count)d cute %(animal)s' % animal_dict    # Форматирование строки с помощью словаря
print(Line)

dinner_plate = 'My dinner plate contains {0}, {1}, {2} and {3}'
dinner_plate =dinner_plate.format('eggs', 'bacon', 'sausage', 'onion')    # Форматирование по индексу
print(dinner_plate)
