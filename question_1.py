import json 

a=open('question.json','r')
s=a.read()
c=json.loads(s)
print(type(c))
print(c)