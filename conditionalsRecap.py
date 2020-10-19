#Conditionals in Python recap
#============================
print( )
print("If-else conditions in python...")
print('==========================')
x = 3
y = 4

if(x == y):
	z = x + y
	print(z)
else:
	print("They are not equal")

print('--------------------------')
print( )
print("El-if conditions in python...")
print('==========================')
x = 5
y = 4

if(x == y):
	print("x and y are equal")
elif(x > y):
	print("x is greater than y")
else:
	print("They are not equal, x is smaller than y")

print('--------------------------')
print( )
print("Playing with conditions in python...")
print('==========================')
x = "fade"
y = input("enter password ")

if(x == y):
	print("x and y are equal, password correct.")
else:
	print("They are not equal")

print('--------------------------')
print( )
print("Multiple conditions in python...")
print('==========================')
x = 3
y = 3
z = 4

if(x == y and x == z):
	print("x, y and z are all equal")
elif(x == y and x != z):
	print("x is equal to y, but different from z")
else:
	print("x, y and z are all different")

print('--------------------------')