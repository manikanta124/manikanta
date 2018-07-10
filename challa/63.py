import csv
header=["symptoms","disease","advices"]
fp=open("kumar.csv",'w')
csv_writer=csv.DictWriter(fp,fieldnames=header)
csv_writer.writeheader()
def inputs():
    lst=dict()
    lst.clear()
    symptoms=input("enter the symptoms:")
    disease=input("enetr the disease:")
    advices=input("enter the advice:")
    lst.setdefault("symptoms",symptoms)
    lst.setdefault("disease", disease)
    lst.setdefault("advices",advices)
    print(lst)
    return lst
csv_writer.writerow(inputs())

s=input("enter symptoms:")
with open("kumar.csv") as csvfile:
    readcsv=csv.reader(csvfile)
    for row in readcsv:
        if s in row[0]:
            print("the disease is:",row[1])
            print("preacautions are:",row[2])