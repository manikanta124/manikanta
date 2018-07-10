import csv
header=["Name","Age","Gender"]

def inputs():
    lst=[]
    lst.clear()
    name=input("Enter Name:")
    age=input("Enter Age:")
    Gender=input("Enter gender:")
    lst.append(name)
    lst.append(age)
    lst.append(Gender)
    return lst

def writerow_user():
    csv_writer.writerow(inputs())

def Modify():
    data=[]
    number = int(input("Enter Number:"))
    wp = open("spl.csv", 'r')
    csv_reader = csv.reader(wp)
    for i in csv_reader:
        data.append(i)
    print(data)
    lst=inputs()
    print(lst)
    wp.close()
    data[number]=lst
    print(data)
    fp= open("spl.csv", 'w')
    csv_writer = csv.writer(fp)
    for i in data:
        if bool(i):
            csv_writer.writerow(i)
    fp.close()
wp=open("spl.csv",'a+')
csv_writer=csv.writer(wp)
Modify()
