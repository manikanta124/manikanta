import csv
s=input("enter id:")
with open("spl.csv") as csvfile:
    readcsv=csv.reader(csvfile)
    print(type(readcsv))
    for row in readcsv:
        print(row[4])
        if s in row:
            print("the employee details is:","name:",row[1],"age:",row[2],"address:",row[3],"salary:",row[4],"height:",row[5],"weight:",row[6])