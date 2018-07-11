s='abc'
L=[]
for i in s:
    if(type(i)==list):
        L.extend(i)
    else:
        L.append
print(list(map(str,s)))
    
