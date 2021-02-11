
import json

dic={
    "shopping_list":
        { 
            "chaco":"15",
            "Biscuits":"50",
            "Diary_milk":"30",
            "ice_cream":"20",
        } 
}


user=input("enter which item you want--")

del dic['shopping_list'][user]

print(dic)

user1=input("enter which item you want to add--")

user2=int(input("enter how many item you want to add--"))

dic['shopping_list'][user1]=user2

print(dic)

with open('shopping_list.json','w') as data:
    json.dump(dic,data,indent=4)


