#Exception Handling
try:
    a=5
    b=7
    print(a+b)
except:
    print("There was an error")
finally:
    print("Code run sucessfully")

#Raise Exception
try:
    a=5
    b=7
    print(a+b)
    raise Exception("qwerty")
except:
    print("There was an error")
finally:
    print("Code run sucessfully")

#
try:
    a = (1,2,3,'hello')
    for i in a:
        
        print(i)
        print(isinstance(i,int))
        if(isinstance(i,int)):
            continue
        else:
            raise Exception()
except:
    print("There was an error")
finally:
    print("Code run sucessfully")

#class
class myClass:
    x = 5

#object
c1 = myClass

# def __init__ Funciton
# def __str__ Function

#constructor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("Azay", 21)

print(p1)

#
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("Azay", 21)

print(p1.name, p1.age)

#Math function
import math

print(math.pi)

import json

jsondata = '{"brand" : "fond"}'

a = json.loads(jsondata)
print(a['brand'])