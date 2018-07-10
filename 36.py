#36. l=[1,2,3,[4,5,6],7,[8,9,10]] for single dimentional list
l=[1,2,3,[4,5,6],7,[8,9,10]]
L=[]
for i in l:
    if(type(i)==list):
        L.extend(i)
    else:
        L.append(i)
print(L)
    
