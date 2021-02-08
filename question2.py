import json
f={"Name":"Ram", 
"Class":"IV", 
"Age":9 }

with open("question2.json","w") as data:
    json.dump(f,data,indent=2)