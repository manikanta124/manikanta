#24. Write a program to findout biggest number in the given numbers.
L=[]
n=input()
for i in range(1,n+1):
    num=input("elemnts")
    L.append(num)
print(L)
L.sort()
print(L[n-1])
