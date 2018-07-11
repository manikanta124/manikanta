#input = 1,2,3,4,5,6,8,10 output = odd,even,odd,even,odd,even,even,even
l=input("enter")
L=[]
s=""
for i in range(0,l):
    ele=input("elemts")
    L.append(ele)
print(L)
for i in L:
    if(i%2==0):
        s=s+","+"even"
    else:
        s=s+","+"odd"
print(s)
        
