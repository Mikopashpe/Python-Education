'''
Переменные необходимы для хранения данных. Название переменной ставится слева от знака присвоения значения данной переменной.
В названиях переменных не допускается использование некоторых специальных символов, также не допускается 
использование числовых значений вначале имени переменной.
Наименование переменной должно быть лаконичным и отражать ее суть.
'''

# *s = 5  При выводе на экран значения данных переменной, мы получим ошибку SyntaxError
# print(*s) 


_s = 15    #Данный специальный символ допускается в присвоении имени переменной. Результат выводится
print(_s)

# 1f = {1, 2, 3, 4, 5, 6, 7}    Аналогичная синтаксическая ошибка появляется при использовании цифр в начале именования переменной
# print(1f)

f1 = (2, 4, 6, 8, 10)    #В данном случае на экран выводится кортеж. Ошибок нет.
print(f1)

a, b, c = 1, 2, 3    #Также можно использовать множественное присваивание значений переменным
print(b, c, a)

a = b-c    #При соблюдении определенных условий, значение переменной можно также присвоить путем манипуляций с другими переменными
print(a)

#Не рекомендуется присваивать переменным зарезервированные в Python имена 

