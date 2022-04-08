from dataclasses import replace

'''
В данном файле рассматривается часть строковых методов
'''

random_line = 'jytbdu, ytbdfuytn, ioyuynk, tery'
c = 'computer'

print(c.find('pu'))    # Метод помогает найти место искомой части

print(c.replace('r', 'rs'))    # Данный метод позволяет заменить одну часть строки на другую, не изменяя в конечном итоге строку

print(c.upper())    # Позволяет сделать все буквенные символы строки в верхнем регистре

print(c.isalpha())

print(random_line.split(','))    # Данные метод позволяет разделить строку по переданному параметру
print(random_line.split('y'))

print((c + 's' == c.__add__('s')),  c)    # Проверяем на равенство два способа изменения выводимой строки. Сама строка не меняется

