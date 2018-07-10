#20. Take two numbers from the user a,b check whether a is divisible by b or not?
a=input("enter number1:")
b=input("enter number2:")
if(a>b):
    if(a%b==0):
        print("a is divisible by b")
    else:
        print("a is not divisible by b")
else:
    print("please enter b as lesser than a")
