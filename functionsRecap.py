#Functions in Python recap
#=========================
print( )
print("User Input in python...")
print('==========================')
print('For using strings:')
x = input('Write the first value ')
print("x = input('Write the first value ')")
print(x)
y = input("Write the second value, don't forget the space ")
print("y = input('Write the second value, don't forget the space ')")
print(y)
print('For string concatenation:')
z = x + y
print('z = x + y')
print(z)
print('- - - - - - - - - - - - - -')
print('For using numbers:')
b = input('Write the third value, integer ')
c = input('Write the fourth value, integer ')
a = int(b) + int(c)
print('z = int(x) + int(y)')
print(a)
print('--------------------------')
print( )
print("Converters in python...")
print('==========================')
celsius = input('Enter the temperature in celsius ')
celsius = int(celsius)
farenheit = (9/5)*celsius + 32
print("farenheit = (9/5)*celsius + 32")
print(int(farenheit))
print('- - - - - - - - - - - - - -')
minutes = input('Enter a number of minutes here ')
seconds = input('Enter a number of seconds here ')
hours = int(minutes)/60 + int(seconds)/3600
print("hours = int(minutes)/60 + int(seconds)/3600")
print(hours)
print('--------------------------')
print( )
print("Basic concept of a function in python...")
print('==========================')
def add(x,y):
	z = x + y
	return z

a = 3
b = 5
c = add(a,b)
print('c = add(a,b)')
print(c)
print('--------------------------')
print( )
print("Functions and User Input in python...")
print('==========================')
def add(x,y):
	z = x ** y
	return print(z)

a = input('Enter the first value ')
b = input('Enter the second value ')
a = int(a)
b = int(b)
add(a,b)
print('--------------------------')
print( )
print("Using a default Parameter in python...")
print('==========================')
def add(x,y = 12):
	z = x - y
	return print(z)

a = input('Enter the first value ')
a = int(a)
add(a)
print('--------------------------')
print( )
print("Using converters in functions in python...")
print('==========================')
def temp(c):
	f = (9/5)*c + 32
	return print(f)

c = input('Enter the temperature in celsius ')
c = int(c)
temp(c)
print('- - - - - - - - - - - - - -')
def time(m,s):
	h = m/60 + s/3600
	return print(h)

m = input('Enter the nr of minutes here ')
m = int(m)
s = input('Enter the nr of seconds here ')
s = int(s)
time(m,s)
print('--------------------------')
print( )
print("Using if/else in python...")
print('==========================')
def divide(x,y):
	if(y == 0):
		return print("Nope, can't compute that, no dividing by zero!")
	else:
		z = x / y
		return print(z)
	
x = input('Enter the first value ')
y = input('Enter the divider here ')
divide(int(x), int(y))
print('--------------------------')