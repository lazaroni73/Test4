import json
from mymodule import person1


print(person1["age"])

x =  '{ "name":"John", "age":33, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

        