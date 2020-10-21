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