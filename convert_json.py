import json

dic={"name":"akshara","age":"18"}

with open('convert_json.json','w') as data:
    json.dump(dic,data,indent=4)
    