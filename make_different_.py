import json

jobj_dict =  '{"name": "David", "age": 6, "class": "I"}'
jobj_list =   '["Red", "Green", "Black"]'
jobj_string = '"Python Json"'
jobj_int = '1234'
jobj_float =  '21.34'

# python_dict=json.loads(jobj_dict)
# print(python_dict)
print(type(jobj_dict))

var = json.loads(jobj_dict)
var1 = json.loads(jobj_list)
var2 = json.loads(jobj_string)
print(var)
print(type(var))
print(type(var1))