L=[]
L1=[]
def remove_occurence(L,ele):
    print(L)
    for i in L:
        if(i is not ele):
            L1.append(i)
    return L1




n=input("num of elements")
for i in range(n):
    ele=input("elements"+str(i)+":")
    L.append(ele)
occ=input("element to remove")
print(remove_occurence(L,occ))

