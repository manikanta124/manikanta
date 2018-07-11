#5. take a string from the user and check contains only digits or not?
str=raw_input("enter the string")
count=0
for i in str:
    if(i.isdigit()):
        count+=1

if(count==len(str)):
    print("given string contains only digits")
else:
    print("given string contains other than digits")
