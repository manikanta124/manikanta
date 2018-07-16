import os
import re
import sys
import time
import unittest,time
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
#print(d)
jsn=d
jsn=json.dumps(jsn)
loaded_jsn=json.loads(jsn)
print(loaded_jsn['rating'])
print(type(jsn))
print(type(loaded_jsn))
"""
r = {'is_claimed': 'True', 'rating': 3.5}
r = json.dumps(r)
loaded_r = json.loads(r)
loaded_r['rating'] #Output 3.5
type(r) #Output str
type(loaded_r) #Output dict
"""