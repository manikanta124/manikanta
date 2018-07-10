import csv
s=input("enter symptoms:")
with open("kumar.csv") as csvfile:
    readcsv=csv.reader(csvfile)
    #print(readcsv)
    for row in readcsv:
        if s in row[0]:
            print("the disease is:",row[1])
            print("preacautions are:",row[2])