#13. take a string from the user and check contains atleast one chars or not?
str=raw_input("enter the string")
count=0
for i in str:
    flag=i.isalpha() or i.isdigit()
    #print(flag)
    if(flag==False):
        count+=1
#print(count)
if(count>=1):
    print("given string contains atleast one special characters")
else:
    print("given string doesn't contain any special characters ")


