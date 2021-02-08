import json 

file_name='text_into_json.txt'
dict={}
with open(file_name) as data:
    for i in data:
        key,Value=i.strip().split(None,1)
        dict[key]=Value.strip()
out_file=open("text_into.json","w")
json.dump(dict,out_file,indent=4)
out_file.close()
