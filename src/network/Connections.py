import json
# examples
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse
y = json.loads(x)

# controll
print(y["age"]) 