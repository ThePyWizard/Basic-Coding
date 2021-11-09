#STACK OPERATION
def isempty(x):
    if x==[]:
        return True
    else:
        return False
def push(x,item):
    x.append(item)
    top=len(x)-1
def pop(x):
    if isempty(x):
        return "Underflow"
    else:
        item=x.pop()
        if len(x)==0:
            top=None
        else:
            top=len(x)-1
            return item
def peek(x):
    if isempty(x):
        return "Underflow"
    else:
        top=len(x)-1
        return x[top]
def display(x):
    if isempty(x):
        print("Stack empty")
    else:
        top=len(x)-1
        print(x[top],'<--top')
        for a in range(top-1,-1,-1):
            print(x[a])
stack=[]
top=None
while True:
    print("Stack operations")
    print("1.Push")
    print("2.Pop")
    print("3.Peek")
    print("4.Display")
    print("5.Exit")
    ch=int(input("Enter your choice(1 to 5) :"))
    if ch==1:
        item=int(input("Enter item"))
        push(stack,item)
    elif ch==2:
        item=pop(stack)
        if item=='Underflow':
            print("Underflow ! Stack is empty")
        else:
            print("Popped item is",item)
    elif ch==3:
        item=peek(stack)
        if item=="Underflow":
            print("Underflow!stack is empty")
        else:
            print("Topmost item is",item)
    elif ch==4:
        display(stack)
    elif ch==5:
        break
    else:
        print("Invalid choice")
