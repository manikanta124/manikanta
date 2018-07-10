

source=input("enter the source file:")
destination=input("enter the destination file:")
fp=open(source,'r')
data=fp.read()
s=open(destination,'w')
s.write(data)
fp.close()
s.close()




"""fp=open(source,"r")
data=fp.read()
wf=open(destination,"w")
wf.write(data)
fp.close()
wf.close
"""