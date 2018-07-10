"""
30. Take actuual string, soucrce string, destination string. replce first nth occurances of soucestring with destination string of actual string

"""
str=raw_input("string")
source=raw_input("sourcestring")
dest=raw_input("destination")
n=input("occurence")
count=0
s=" "
l=len(str)-len(source)+1
for i in range(0,l):
    #print(str[i:(len(s)+i)])
    if(str[i:(len(source)+i)]==source):
        count+=1
        if(count==n):
            str=str[:i]+dest+str[i+len(dest):]
#print(count)
print(str)
