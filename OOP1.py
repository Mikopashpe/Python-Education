'''
В данном разделе идет ознакомление с ООП на ЯП Python.
В рамках урока рассматривается создание электронного кошелька.
'''

# Создание класса
class Purse:
    # Инициализация класса и его аргументов
    def __init__(self, valuta, name = 'Unknown'):
        if valuta not in ('USD', 'EUR'):
            raise ValueError
        self.__money = 0.00
        self.valuta = valuta
        self.name = name

    # Функция пополнения баланса
    def top_up_balance(self, howmany):
        self.__money = self.__money + howmany
        return howmany

    # Функция списания средств с кошелька
    def top_down_balance(self, howmany):
        self.__money = self.__money - howmany
        if self.__money - howmany < 0:
            print('Недостаточно средств на балансе')
            raise ValueError ('Недостаточно средств')
        return howmany

    # Функция удаления кошелька
    def __del__(self):
        print('Кошелек удален')  
        
    # Функция запроса информации о состоянии счета
    def info(self):
        return self.__money



x = Purse('USD')
y = Purse("EUR")
x.top_up_balance(200)
y.top_up_balance(x.top_down_balance(20))
print(x.info())
print(y.info())

