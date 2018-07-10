from __future__ import print_function
n=input("enter")
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j==n or j==1 or i==n or i==1):
            print('1',end="")
        else:
            print('0',end="")
    print("\r")
