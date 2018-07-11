#57. WAP to do all queue operations using lists
n=5
class Queue:
    def __init__(self):
        self.L=[]
        self.size=0

    def enqueue(self,num):
        if(self.size<n):
            self.size+=1
            self.L.insert(0,num)
        
    def dequeue(self):
        self.L.pop()
    def size(self):
        return(len(self.L))
    def display(self):
        print(self.L)
    def isempty():
        if(len(self.l)==0):
            print("queue is empty")
    def front_ele(self):
        l=len(self.L)
        print("front elemnt is:",self.L[l-1])
    def rear_ele(self):
        print("rear element is"self.L[0])
que=Queue()
while(1):
    print("1:enqueue")
    print("2:dequeue")
    print("3:size")
    print("4:display")
    print("5:isempty")
    print("6:front")
    print("7:rear")
    print("8:exit")
    choice=input("which function")
    if(choice==1):
        for i in range(0,n):
            ele=input("ele")
            que.enqueue(ele)
    elif(choice==2):
        que.dequeue()
    elif(choice==3):
        print("size of queue",que.size())
    elif(choice==4):
        print("the queue is:",que.display())
    elif(choice==5):
        que.isempty()
    elif(choice==6):
        que.front_ele()
    elif(choice==7):
        que.rear_ele()
    elif(choice==8):
        exit()
    
        




