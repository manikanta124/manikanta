#25. findout third occurance of given substring
str=raw_input("string")
s=raw_input("substring")
count=0
l=len(str)-len(s)+1
for i in range(0,l):
    print(str[i:(len(s)+i)])
    if(str[i:(len(s)+i)]==s):
        count+=1
        if(count==3):
            print(i)
print(count)
    
