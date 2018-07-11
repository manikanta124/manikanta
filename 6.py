#6. take a string from the user and check contains only  alphabets or not?
str=raw_input("enter the string")
count=0
for i in str:
    if(i.isalpha()):
        count+=1
#print(count)
if(count==len(str)):
    print("given string contains only alphabets")
else:
    print("given string contains other than alphabeta")
