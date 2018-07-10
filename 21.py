"""
21. Given an age, figure out whether someone's a baby, toddler, child, teenager, adult or old codger.
"""
age=input("enter age:")
if(age<2):
    print("baby")
elif(age>=2 and age<=3):
    print("toddler")
elif(age>3 and age<13):
    print("child")
elif(age>=13 and age<18):
    print("teenager")
elif(age>=18 and age<35):
    print("adult")
else:
    print("old codger")

