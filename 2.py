str=raw_input("enter string")
s=raw_input("enter substring")
count=0
for i in range(len(str)):
    if(str[0:i+1]==s):
        count+=1
if(count>=1):
    print("given substring is present in actual string")
else:
    print("given substring is not  present in actual string")
    
