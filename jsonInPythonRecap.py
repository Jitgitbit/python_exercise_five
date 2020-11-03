import json
#FileHandling in Python recap
#============================
print( )
print("Json convertion in python...")
print('==========================')

x = {"name":"Jason" , "age":33 , "job":"developer"}

y = json.dumps(x)
print(y)

print('- - - - - - - - - - - - - -')

a = '{"name":"Jason" , "age":33 , "job":"developer"}'

b = json.loads(a)
print(b)

print('--------------------------')