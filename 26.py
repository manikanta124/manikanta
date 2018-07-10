#26. findout nth occurance of given substring

str=raw_input("string")
s=raw_input("substring")
n=input("occurence")
count=0
l=len(str)-len(s)+1
for i in range(0,l):
    #print(str[i:(len(s)+i)])
    if(str[i:(len(s)+i)]==s):
        count+=1
        if(count==n):
            print(i)
#print(count)
    
