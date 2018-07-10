
import csv
L=[]
for i in range(0,3):
    ele=raw_input("ele")
    L.append(ele)
file=open('output.csv','w')
read=csv.writer(file)
for i in L:
    
    print(i)
 
    read.writerow([i])
    L=[]


    
