#8. take a string from the user and check contains only  capiatl letters or not?
str=raw_input("enter the string")
count=0
for i in str:
    if(i.isupper()):
        count+=1
print(count)
if(count==len(str)):
    print("given string contains only Capital alphabets")
else:
    print("given string contains other than Capital alphabets")


