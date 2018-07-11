#18. Determine the factors of a number entered  by the user
num=input("enter the number")
for i in range(1,num+1):
    if(num%i==0):
        print(i)
