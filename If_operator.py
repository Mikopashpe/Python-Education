'''
В данном разделе происходит ознакомление с оператором if.
'''
choice = input('Chooce your product: ')
food_dict = {'ham' : 1.69, 'cheese' : 1.79, 'bread' : 0.36}
if choice == 'ham':    # Данный код - пример множественного ветвления
    print(food_dict['ham'], '£')
elif choice == 'cheese':
    print(food_dict['cheese'], '£')
elif choice == 'bread':
    print(food_dict['bread'], '£')
else:
    print('Bad choice!')

try:    # Перехват и обработка исключений
    print(food_dict[choice])
except:
    print('Bad choise!')

a = 'true' if 'word' else 'false'    # Непустые строки означают истину
print(a)

a = 'true' if '' else 'false'    # Пустые строки означают ложь
print(a)