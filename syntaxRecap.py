#Python syntax recap
#===================
print('variables and constants...')

x = 5 
y = 3
z = 7
q = 'word'
a = 'the '

print('x = ')
print(x)
print('x + y = ')
print(x + y)
print('q = ')
print(q)
print('a + q = ')
print(a + q)

print('--------------------------')
print('numbers...')

print("8 / 3 = ")
print(8 / 3)
print("2 ** 3 = ")
print(2 ** 3)
# arithmetic sequence: **, * /, + -
print(" 1 + 2 * 3 ** 4 / 5 - 6 = ")
print( 1 + 2 * 3 ** 4 / 5 - 6)
print(' ((1 + 2) * 3) ** 4 / 5 - 6 = ')
print( ((1 + 2) * 3) ** 4 / 5 - 6)

print('--------------------------')
print('dynamic typing...')

b = "Alex"
b = "blah"
b = 1234
print("b = ")
print(b)

print('--------------------------')
print('restrictions on data types naming...')

print("a-z, A-Z, 0-9, and _ are allowed")
print("@ and % are not allowed")
print("numbers can not be placed in the beginning of the name!")

print('--------------------------')
print('casting, or changing type...')

x = 2
print("x = ")
print(x)

x = float(2)
print("x = ")
print(x)