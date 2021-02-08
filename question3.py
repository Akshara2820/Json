import json

f={"Name":"Ram", 
"Class":"IV", 
"Age":9 }


with open('question.json','w') as data:
    data=json.dumps(f,indent=4)
    print(type(data))
    print(data)

