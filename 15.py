#15. take a string from the user and check contains atleast one small letter or not?
str=raw_input("enter the string")
count=0
for i in str:
    if(i.islower()):
        count+=1
#print(count)
if(count>=1):
    print("given string contains atleast  onesmall alphabets")
else:
    print("given string doesn't contain any small alphabets")


