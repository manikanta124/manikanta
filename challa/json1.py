import os
import re
import json

file=open("/Users/machalla/Documents/built_integrations_programs/Task/Python_adb/test.txt","r+")
buffer=file.readlines();
#print(buffer)
s="commit"
l1=[]
l2=[]
value=[]
for line in buffer:
    if s in line:
        l1.append(line)
        if not l2==[]:
            value.append(l2)
            l2=[]
    else:
        l2.append(line)
#print(l2)
#print(value)
#print(l1)
d=dict(zip(l1,value))
print(d)
jsn1=d
with open("log.json","w") as fp:
    fp.dump(d,fp)
#js=json.dumps(jsn)
#print(js)
#print(dir(json))