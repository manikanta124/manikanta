#12. take a string from the user and check contains atleast one alphabets or not?
str=raw_input("enter the string")
count=0
for i in str:
    if(i.isalpha()):
        count+=1

if(count>=1):
    print("given string contains atleast one alphabet")
else:
    print("given string doesn't contain any  alphabet")
