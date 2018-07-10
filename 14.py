#14. take a string from the user and check contains atleast one capital letter or not?
str=raw_input("enter the string")
count=0
for i in str:
    if(i.isupper()):
        count+=1
#print(count)
if(count>=1):
    print("given string contains atleast one Capital alphabets")
else:
    print("given string doesn't contains any Capital alphabets")
