list=[1,23,323,12,121,12,1]
s=set(list)
print(s)

#another way
list=[1,2,3,5,1,6,2,9,8,4,5,4]
cnt=0
for i in range(len(list)):
    if list[i]==list[0]:
        for j in range(len(list)):
            if list[j]!=list[j+1]:
                print("no duplicates found")
            else:
                    cnt=cnt+1
if cnt==len(list):
    print("dupliactes found")
