"""
l = [0,1,2]
l1 = [3,4,5]
s = dict(zip(l, l1))
print(s)

def ispoweroftwo(n):
if (n == 0):
return False
while (n != 1):
if (n % 2 != 0):
return False
n = n // 2

return True
print(ispoweroftwo(64))

"""
s = input("enter a string:")
fb=[]
cnt=0
with open("/Users/machalla/device.txt") as f:
    fb = f.read()
    print(fb)
    for line in fb:
        print(line)
        if (s==line):
            cnt+=1
print(cnt)