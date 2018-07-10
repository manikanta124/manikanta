q=["mani","ram","krish"]
def isempty(q):
    return q==[]
def push(q):
    q.append("mani")
    print(q)
def insert(q):
    q.insert(0,"challa")
    print(q)
def delete(q):
    print(q.pop())
    print(q)
def size(q):
    print(len(q))


isempty(q)
push(q)
insert(q)
delete(q)
size(q)