s="abbcdefgghijjkllmnopqqrstuvwwk"
l=list(s)
s1=s[::-1]
s=""
l1=[]
for i in range(1,len(l)):
    j=i-1
    if l[i]!=l[j]:
        l1.append(l[i])
        print(l1)

    else:
        if (len(l1)!=0):

            del(l1[-1])
print(l1)

for i in range(0,len(s1)):
    if s1[i]==l1[-1]:
        if s1[i-1]==s1[i-2]:

           del(l1[-1])
           break
for i in l1:
    s+=i
print(s)
