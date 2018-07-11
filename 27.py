#27. Taake some single digit numbers from the user and findout min, maximum, sum, average
L=[]
n=input("number of elemnts")
for i in range(1,n+1):
    num=input("elemnts")
    L.append(num)
print(L)
L.sort()
min=L[0]
for i in L:
    if(i<min):
        min=i
sum=0
for i in L:
    sum+=i
print(min)
print(L[n-1])
print(sum)
avg=sum/n
print(avg)
