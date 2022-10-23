import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x
y = json.loads(x)

# The result is a python dictionary
print(y["age"])


x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# Converts into json
y = json.dumps(x)

# print
print(y)


import json

#print(json.dumps({"name": "John", "age": 30}))
#print(json.dumps(["apple", "bananas"]))
#print(json.dumps(("apple", "bananas")))
#print(json.dumps("hello"))
#print(json.dumps(42))
#print(json.dumps(31.76))
#print(json.dumps(False))
#print(json.dumps(None))


import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}


print(json.dumps(x))

json.dumps(x, indent=4)

json.dumps(x, indent=4, separators=(". ", " = "))

json.dumps(x, indent=4, sort_keys=True)



