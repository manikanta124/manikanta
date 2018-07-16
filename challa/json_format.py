import json
l1=[]
l2=[]
d={}
jp=open("j4_log.json","w")
f=open("/Users/machalla/Documents/built_integrations_programs/Task/Python_adb/test.txt","r")
for line in f.readlines():
    if "commit" in line and len(d)!=0:
        l2.append(d)
        d={}

    if "commit" in line:
        l1=line.split()
        d[l1[0]]=l1[1]
    elif "Date" in line:
        l1=line.split('Date:')
        d["Date"]=l1[1][:-1]
    elif "Author" in line:
        l1=line.split('Author:')
        d["Author"]=l1[1][:-1]
    elif not line=='\n':
            d["msg"]=line[:-1]
json.dump(l2, jp, indent=4, separators=(',',':'))
jp.close()

