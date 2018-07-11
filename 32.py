#32. l=[10,20,30,[40,50,60],70,[80,90,20]]. Convert this list as sigle dimentiona list
l=[10,20,30,[40,50,60],70,[80,90,20]]
L=[]
for i in l:
    if(type(i)==list):
        L.extend(i)
    else:
        L.append(i)
print(L)
