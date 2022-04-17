'''
В данном разделе рассматриваются основыработы с циклом while.
'''

x = 'apple'
while x:
    print(x, end = ' ')    # apple pple ple le e
    x = x[1:]


a = 0
b = 10

while a < b:
    print(a, end = ' ')    # 0 1 2 3 4 5 6 7 8 9
    a += 1


x = 28
l = []

while x:
    x -= 1
    if x % 2 == 0:
        continue
    l.append(x)
    l.sort()
print(l)    # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27]


