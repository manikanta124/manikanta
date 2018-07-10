"""char=0
words=1
str="manikanta kumar challa"
for i in str:
    char=char+1
    if(i==" "):
        words=words+1
print(char)
print(words)
"""
"""fname = input("Enter file name: ")
print(fname)
num_lines = 0
with open(fname, 'r') as f:
    print(f)
    for line in f:
        num_lines += 1
print("Number of lines:")
print(num_lines)
"""
fn = input("Enter file name: ")
num_lines = 0
f=open(fn, 'r')
print(f)
for line in f:
    num_lines += 1
print("Number of lines:")
print(num_lines)