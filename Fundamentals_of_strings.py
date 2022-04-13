'''

'''

from dataclasses import replace


a, b = 'apple', "apple"    #
print(a == b)

a, b = 'knight\'s', "knight\"s"    #
print(a, b)

s = 'some\n\tbod\n\t\ty'    #
print(s)
print(len(s))

s = 'C\\p\\m'    #
print(s)

S = 'Spam'
print(S[0], S[-3], S[2], S[-1])
print(S[0] == S[-4])
print(S[0:3])
print(S[0::1])
print(S[::-1])

x = 44
y = '44'
print(x + int(y))
print(y + str(x))

print(ord('*'))
print(chr(101))

s = 'Nein!'
s = s + 'Mein'
print(s)
s = s[:4] + 'Auf' + s[-5]
print(s)

e = 'cameltown'
e = e.replace('ltown', 'rton')
print(e)

t = 'This is %d %s texts' % (1, 'of')
print(t)

w = 'This is {0} {1} texts'.format(1, 'of')
print(w)

r = s.find('ei')
print(r)

longword = 'itegbtyuXXXXiwetryhiwtXXXXiuryewityihiXXXX'
longword = longword.replace('XXXX', 'YYY', 2)
print(longword)

L = list(longword)
print(L)

L[12] = 'bbbbbb'
L[2] = 'FRFRRFR'
print(L)

longword = ''.join(L)
print(longword)

print(longword.split('i'))

animal_dict = {'animal' : 'cat', 'count' : 1}
Line = 'i have %(count)d cute %(animal)s' % animal_dict
print(Line)

dinner_plate = 'My dinner plate contains {0}, {1}, {2} and {3}'
dinner_plate =dinner_plate.format('eggs', 'bacon', 'sausage', 'onion')
print(dinner_plate)
