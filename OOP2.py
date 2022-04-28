'''

'''

# Создание тренировочного класса и присвоение ему атрибутов
class Nameclass:
    firstattr = 'color'
    secattr = 2

# Создание экземпляров родительского класса
a = Nameclass()
b = Nameclass()

# Субклассам доступны все атрибуты родительского класса
print(a.firstattr)
print(b.secattr)

a.firstattr = 'another'
# При локальном изменении атрибута в субклассе, значение атрибута в родительском классе не меняется
print(a.firstattr)
print(Nameclass.firstattr)

# Добавление нового атрибута
setattr(Nameclass, 'thirdattr', [1, 2, 3, 4])
print(Nameclass.__dict__)

# Удаление атрибута в субклассе заменяет его атрибутом родительского класса
delattr(a, 'firstattr')
print(a.firstattr)

# Проверка наличия атрибута по имени. Результат - булево значение
print(hasattr(Nameclass, 'secattr'))

# Получение значениия атрибута
print(getattr(Nameclass, 'secattr'))

# Создание новых атрибутов
a.x = 1
b.y = {23, 45, 56}
print(a.__dict__)
print(b.__dict__)

# Удаление атрибута
del a.x
print(a.__dict__)

