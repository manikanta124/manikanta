

a=int(input("enter first a number:"))
b=int(input("enter the second number:"))
print(a+b)
if(a>b):
    print("a is bigger number")
else:
    print("b is bigger number")


#biggest numbers in the given numbers
list=[10,20,4,1,12,56,21,32]
max=0
for i in list:
    if(i>max):
        max=i
print("the maximum number is ",max)



#take a single digit numbers and find sum.avg,max,min

list=[]
sum=0
for i in range(0,5):
    list=input("enter the numbers:")
print(list)
for i in list:
    sum=sum+i
print(sum)

def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((10,20,30)))

#anotherway

n=int(input("number of elements to be entered:"))
x=0
mx=0
mn=0
list=[]
for i in range(0,n):
    elem=int(input("enter the elements:"))
    x+=elem
    list.append(elem)
print(sum(list)/n)
print(x)
print(x/n)
print(list)
for i in list:
    if(i>mx):
        mx=i
print(mx)
mn=list[0]
for i in list:
    if(i<mn):
        mn=i
print(mn)

