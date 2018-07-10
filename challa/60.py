import csv
header=["project","period","members"]
fp=open("mani.csv",'a+')
csv_writer=csv.DictWriter(fp,fieldnames=header)
csv_writer.writeheader()
def inputs():
    lst=dict()
    lst.clear()
    project=input("Enter project:")
    period=input("Enter period:")
    members=input("Enter members:")
    lst.setdefault("project",project)
    lst.setdefault("period", period)
    lst.setdefault("members", members)
    print(lst)
    return lst
csv_writer.writerow(inputs())
#csv_writer.writerow(inputs())


def Modify():
    data=[]
    number = int(input("Enter Number:"))
    wp = open("mani.csv", 'r')
    csv_reader = csv.DictReader(wp,fieldnames=header)
    print(csv_reader.fieldnames)
    dict_reader=csv_reader.reader
    for i in dict_reader:
        data.append(i)
    print(data)
    lst=inputs().values()
    wp.close()
    data[number]=lst
    print(data)
    fp= open("mani.csv", 'w')
    csv_writer = csv.writer(fp)
    for i in data:
        if bool(i):
            csv_writer.writerow(i)
    fp.close()

Modify()