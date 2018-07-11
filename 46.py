#46. Find third max value of element in a list with soring and without sorting a list.
n=input("number of elements")
L=[]
for i in range(0,n):
    ele=input("elements"+str(i))
    L.append(ele)
#L.sort()
print(L)
#print(L[n-3])
m1=L[0]
m2=L[0]
m3=L[0]
for i in L:
    if(i>m1):
        m3=m2
        m2=m1
        m1=i
    elif(i>m2):
        m3=m2
        m2=i
    else:
        m3=i
print(m3)
    
