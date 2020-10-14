#Functions in Python recap
#=========================
print( )
print("User Input in python")
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
print("Converters in python")
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
print("Basic concept of a function in python")
def add(x,y):
	z = x + y
	return z

a = 3
b = 5
c = add(a,b)
print('c = add(a,b)')
print(c)
print('==========================')