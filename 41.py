#41. input: fun(5) output: [1,2,3,4,3,2,1]
def fun(num):
    L=[]
    L1=[]
    for i in range(1,num):
        L.append(i)
    print(L)
    
    L1.extend(L[::-1])
    print(L1)
    L.extend(L1[1:])
    print(L)


n=input("num")
fun(n)
