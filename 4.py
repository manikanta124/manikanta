#4. take a number from the user and check whether it is prime?
num=input("enter the number")
if(num>0):
    for i in range(1,num):
        if(num%i==0):
            print("given number is not prime")
            break
    else:
        print("given number is prime")
