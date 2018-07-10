#9. take a string from the user and check contains only  small letters or not?

str=raw_input("enter the string")
count=0
for i in str:
    if(i.islower()):
        count+=1
#print(count)
if(count==len(str)):
    print("given string contains only small alphabets")
else:
    print("given string contains other than small alphabets")


