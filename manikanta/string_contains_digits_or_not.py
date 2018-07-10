s=input("enter a string:")
if(s.isdigit()):
    print(s,"contains only digits")
else:
    print(s,"is not contain digits")

#aother way
import re
m="manikanta"
s="sravan"
print(bool(re.match("^[0-9]*$",m)))
print(bool(re.match("^[0-9]*$", s)))


#another way
s=input("enter a string:")
for i in s:
if(i>='0' and i<='9'):
    print("the string contain only digits")
else:
    print("the string is not contain digits")

