import json

dic={
 "a":  1,
 "a":  2,
 "a":  3, 
 "a": 4,   
 "b": 1, 
 "b": 2
 }

with open('unique_keys.json','w') as data:
    json.dump(dic,data,indent=2)
