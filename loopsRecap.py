#Loops in Python recap
#============================
print( )
print("For loops in python...")
print('==========================')
variable = ['']
for value in variable:
	pass

x = [1,2,3,4,5,6,7,8,9,10]

for item in x:
	print(item + 111)

print('--------------------------')
print( )
print("For loops with user input in python...")
print('==========================')

x = [0,1,2,3,4,5,6,7,8,9]

for i in x:
	x[i] = input("Enter your name please: ")

print("The new list of names is: ")
print(x)
print('--------------------------')
print( )
print("While loops in python...")
print('==========================')

i = 0

while i < 77:
	print(i)
	i += 12

print('--------------------------')
print( )
print("Looping through a string in python...")
print('==========================')

for i in "Blueberry":
	print(i)

print('--------------------------')
print( )
print("Break statement in python...")
print('==========================')

x = [1,2,3,4,5,6,7,8,9]
for i in x:
	print(i)
	if i == 5:
		break
print('- - - - - - - - - - - - - -')

x = ['red', 'blue', 'yellow', 'green']
for i in x:
	if i == 'yellow':
		break
	print(i)

print('--------------------------')
print( )
print("Continue statement in python...")
print('==========================')

x = [1,2,3,4,5,6,7,8,9]
for i in x:
	if i == 5:
		continue
	print(i)
print('- - - - - - - - - - - - - -')

x = ['red', 'blue', 'yellow', 'green']
for i in x:
	if i == 'yellow':
		continue
	print(i)
	
print('--------------------------')
print( )
print("range() in python...")
print('==========================')

for i in range(4,10):
	print(i)
print('- - - - - - - - - - - - - -')
print("range(starting point, range, order)")

for x in range(0, 101, 5):
	print(x)
	
print('--------------------------')
print( )
print("Else in for loop in python...")
print('==========================')

for x in range(10):
	print(x)
else:
	print("Now all seats are taken, it's over.")
	
print('--------------------------')