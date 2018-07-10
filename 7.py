#7. take a string from the user and check contains only  special chars or not?
str=raw_input("enter the string")
count=0
for i in str:
    flag=i.isalpha() or i.isdigit()
   # print(flag)
    if(flag==False):
        count+=1
#print(count)
if(count==len(str)):
    print("given string contains only special characters")
else:
    print("given string contains other than special characters ")

