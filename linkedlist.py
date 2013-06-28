#Linked List implementation

class node(object):
    x=None
    next=None
    def __init__(self):
        x=None
        next=None

root=None

def init():
    global root
    root=node()
    pass

def insert_end(v):
    global root
    if root.x is None:
        root.x=v
    else:
        c=root
        while not (c.next is None):
            c=c.next
        c.next=node()
        c=c.next
        c.x=v
    pass

def insert_beg(v):
    global root
    if root.x is None:
        root.x=v
    else:
        c=root
        root=node()
        root.x=v
        root.next=c
    pass

def insert_n(n,v):
    global root
    if n==1:
        insert_beg(v)
    c=root
    while not (c.next is None or n ==1):
        c=c.next
        n-=1
    t=c.next
    c.next=node()
    c=c.next
    c.x=v
    c.next=t
    pass

def remove_end():
    global root
    pass

def remove_beg():
    global root
    pass

def remove_n(n):
    global root
    pass

def rev():
    global root
    pass

def trav():
    global root
    if root.x is None:
        print "Empty list"
    else:
        c=root
        while not (c is None):
            print "->",c.x,
            c=c.next
        print
    pass

if __name__=='__main__':

    init()

    while True:
        print "Enter choice:"
        print "0. Re-initialise the list"
        print "1. Traverse list"
        print "2. Insert at end"
        print "3. Insert at root"
        print "4. Remove from root"
        print "5. Remove from end"
        print "6. Insert at middle for a given n"
        print "7. Remove from middle for a given n"
        print "8. Reverse list"
        print "9. Exit"
        print "$Linked-list\_",
        n=input()
        if n==9:
            break
        elif n==0:init()
        elif n==1:trav()
        elif n==2:insert_end(input("Enter value : "))
        elif n==3:insert_beg(input("Enter value : "))
        elif n==4:remove_beg()
        elif n==5:remove_end()
        elif n==6:insert_n(input("Enter n : "),input("Enter value : "))
        elif n==7:remove_n(input("Enter n : "))
        elif n==8:rev()
        else:continue
    
