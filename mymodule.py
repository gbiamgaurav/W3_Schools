
def greeting(name):
    print("Hello " + name)


import mymodule

mymodule.greeting('Gaurav')

person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}

import mymodule

a = mymodule.person1["age"]
print(a)

b = mymodule.person1["country"]
print(b)

c = mymodule.person1["name"]
print(c)

import mymodule as mx

a = mx.person1["age"]
b = mx.person1["name"]
c = mx.person1["country"]
print(a, b, c)

import platform
x = platform.system()
print(x)

import platform

x = dir(platform)
print(x)

from mymodule import person1

print(person1["age"])