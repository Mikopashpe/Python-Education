'''

'''

from errno import ECONNABORTED


a = [1, 2, 3, 4]
b = '56'
print(a + list(b))
print(b + str(a))

print(a[:1], a[:2], a[-1], a[-4])    # Нарезание списка

new_list = [[1, 2, 3], [11, 22, 33], [111, 222, 333]]
print(new_list[1], new_list[2][1])

new_list[1] = 'word'
print(new_list)

new_list[0][0:2] = [15]
print(new_list)

new_list.extend(['doom', 43, 54])
print(new_list)

new_list.append([90, 25])
print(new_list)

second_list = [1, 2]
second_list.extend([3, 4, 5])
print(second_list)

second_list.pop()
print(second_list)

second_list.reverse()
print(second_list)

second_list =list(reversed(second_list))
print(second_list)

print(second_list.index(2))

second_list.insert(2, 15)
print(second_list)

second_list.remove(15)
print(second_list)

second_list.pop(2)
print(second_list)

print(second_list.count(4))

del new_list[2:]
print(new_list)