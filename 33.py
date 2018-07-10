#33 input: "google" print count of each character
str="google"
d={}
cout=d
for i in str:
    if i in cout:
        cout[i]+=1
    else:
        cout[i]=1
print(cout)
