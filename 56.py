n=5
class Stack:
    def __init__(self):
        self.L=[]
        self.size=0

    def push(self,num):
        if(self.size<n):
            self.size+=1
            self.L.append(num)
      
    def pop(self):
        self.L.pop()
    def size(self):
        return(len(self.L))
    def display(self):
        print(self.L)

    def isempty():
        if(len(self.l)==0):
            print("queue is empty")
    

sta=Stack()
while(1):
    print("1:push")
    print("2:pop")
    print("3:size")
    print("4:display")
    print("5:isempty")
    print("6:exit")
    choice=input("which function")
    if(choice==1):
        for i in range(0,n):
            ele=input("ele")
            sta.push(ele)
    elif(choice==2):
        sta.pop()
    elif(choice==3):
        print("size of stack",sta.size())
    elif(choice==4):
        print("the stack is:",sta.display())
 
    elif(choice==5):
        sta.isempty()
    elif(choice==6):
        exit()
    
    
    
