import json


dic={'emp1':{"name":"akshara",'age':'18','education':'bsc'},'emp2':{'name2':'sarika','age2':'19','education2':'12th',}}
with open('make_dict.json','w') as data:
    json.dump(dic,data,indent=6)

