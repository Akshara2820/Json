import json

dic={'4': 5,'6': 7,'1': 3,'2': 4}
s=sorted(dic.values())
dic1={}
for i in s:
    for j in dic.keys():
        if dic[j]==i:
            dic1[j]=dic[j]
            break
print(dic1)


with open('sort_dict_into.json','w') as data:
    json.dump(dic1,data,indent=4)
