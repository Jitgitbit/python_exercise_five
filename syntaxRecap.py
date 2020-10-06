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

print('--------------------------')
print('methods...')

x = "water"
print("x = ")
print(x)
x = x.upper()
print("x = ")
print(x)
x = x.title()
print("x = ")
print(x)
print( )
showMeAllExistingMethodsForStrings = dir("string")
print("showMeAllExistingMethodsForStrings = ")
print( )
print(showMeAllExistingMethodsForStrings)

print('--------------------------')
print('indexing and slicing...')

y = "hello world"
x = y[6]
print("y = ")
print(y)
print("x = ")
print(x)
print( )
z = y.replace('l', 'r')
print("z = ")
print(z)
print( )
w = y[6:11]
print("w = ")
print(w)
print( )
h = y[0:5]
print("h = ")
print(h)
h = y[:5]
print("h = ")
print(h)
print( )
hoei = y[-4:-1]
print("hoei = ")
print(hoei)

print('--------------------------')
print('string formatting...')

x = "Alex"
y = 33
z = f"My name is {x} and my age is {y}"
print("x = ")
print(x)
print("y = ")
print(y)
print("z = ")
print(z)
print( )
x = ["Alex", "sports", "33"]
y = f"Hello, my name is {x[0]}, I am {x[2]} years old and my hobby is {x[1]}."
print("x = ")
print(x)
print("y = ")
print(y)

print('--------------------------')
print('Lists...')

x = ["Alex", "red", "blue", "green", "void", 3, 4.3]
print("x = ")
print(x)
print( )
showMeAllExistingMethodsForLists = dir(list)
print("showMeAllExistingMethodsForLists = ")
print( )
print(showMeAllExistingMethodsForLists)
print( )
y = x[2]
print("y = ")
print(y)
print( )
y = x[-2]
print("y = ")
print(y)
print( )
y = len(x)
print("y = ")
print(y)
print( )
y = x.pop()
print("y = ")
print(y)
print("x = ")
print(x)
print( )
y = x.append("prft")
print("y = ")
print(y)
print("x = ")
print(x)
print( )
y = x.remove("red")
print("y = ")
print(y)
print("x = ")
print(x)

print('--------------------------')
print('Tuples...')

x = ("Alex", "red", "blue", "green", "void", 3, 4.3)
print("x = ")
print(x)
print( )
showMeAllExistingMethodsForTuples = dir(list)
print("showMeAllExistingMethodsForTuples = ")
print( )
print(showMeAllExistingMethodsForTuples)
print( )
y = x[2]
print("y = ")
print(y)
print( )
y = x[-2]
print("y = ")
print(y)
print( )
y = len(x)
print("y = ")
print(y)
print( )
print("Tuples are a lot like lists, except that they can not be edited!")

print('--------------------------')
print('Dictionaries...')

x = {"number": 3, "name": "Alex", "age": 37}
print("x = ")
print(x)
print( )
showMeAllExistingMethodsForDictionaries = dir(dict)
print("showMeAllExistingMethodsForDictionaries = ")
print( )
print(showMeAllExistingMethodsForDictionaries)
print( )
x["age"] = 73
print("x = ")
print(x)
print( )
x["name"] = "Rupert"
print("x = ")
print(x)
print( )
print("The count for length is made in pairs:")
y = len(x)
print("y = ")
print(y)
print( )
print("Adding pairs:")
x["year"] = 1983
print("x = ")
print(x)
print( )
print("Removing pairs:")
x.pop("age")
print("x = ")
print(x)
print( )
print("Dictionaries are also a lot like lists, except that they consist of key:value pairs! (and the key is named)")