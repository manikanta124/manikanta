import os
import re
import sys
import time
import unittest,time
#import json

file=open("/Users/machalla/Documents/built_integrations_programs/Task/Python_adb/test.txt","r+")
buffer=file.readlines();
#print(buffer)
#s=dict(buffer)
#print(s)
y={}
print(x)
for line in buffer:
    key,value=line.strip().split(" ")
    y[key].append(value)
print(y)  

"""y = {} 
infile = open("stuff.txt", "r") 
z = infile.read() 
for line in z: 
    key, value = line.strip().split(':') 
    y[key].append(value) 
print(y) 
infile.close()
"""
"""
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
#js=json.dumps(jsn)
#print(js)
print(dir(json))
"""
