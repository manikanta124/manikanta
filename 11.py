#11. take a string from the user and check contains atleast one digit or not?
str=raw_input("enter the string")
count=0
for i in str:
    if(i.isdigit()):
        count+=1

if(count>=1):
    print("given string contains atleast one digit")
else:
    print("given string doesn't contain any digits")
