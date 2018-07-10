#40. WAP to find union and intersection of lists.
L=[]
L1=[]
n=input("num of elemts")
for i in range(0,n+1):
    ele=input("elemnts")
    L.append(ele)
for i in range(0,n+1):
    ele=input("elemnts")
    L1.append(ele)
s=set(L)
s1=set(L1)
s2=s & s1
s3=s|s1
print(s2)
print(s3)
