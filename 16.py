"""
16. Take the input from the user for(Total number of people, toatl number of busses, Number of seats for bus). Based on the input
	Deside whether there is sufficient busses or not and give solution for how many extra busses required.
"""
people=input("enter the number of people")
buses=input("enter the number of buses")
seats=input("enter the number of seats")
required=(people//seats)
rem=(people%seats)
#print(requried)
#print(rem)
if(required-buses==0 and rem==0):
    print("sufficient buses are here")
else:
    bal=(required-buses)+1
    print(bal)
