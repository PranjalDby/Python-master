# Merge Two Sorted linked List

class Node:
    lenghtLL = 0
    def __init__(self,data):
        self.data = data
        self.next = None
        self.lenghtLL +=1


def insertAtHead(head:Node,data:int)->Node:
    if head == None:
        newNode = Node(data)
        newNode.next = None
        head = newNode

        return head
    
    else:
        newNode = Node(data)
        newNode.next = head
        head = newNode

        return head

def insertAtPosition(head:Node,data:int,index:int):
    if head == None or index == -1 or head.lenghtLL < index:
        return head
    
    if head.next == None:
        newnode = Node(data)
        head.next = newnode
        return head
    
    if index == 0:
        print('insert at head called')
        head = insertAtHead(head,data)
        return head
    
    ptr = head
    prev = None
    currIndx = -1
    
    while currIndx != index-1:
        currIndx +=1
        prev = ptr
        ptr = ptr.next
    
    newnode = Node(data)
    temp = prev.next
    prev.next = newnode
    newnode.next = temp
    return head

def insertElement(head:Node,data):
    if head == None:
        newnode = Node(data)
        head = newnode
        return head
    
    else:
        ptr = head
        prev = None
        while(ptr.next != None):
            prev = ptr
            ptr = ptr.next

        newnode = Node(data)
        prev.next = newnode
        prev = head

        return head

def printLinkedList(head):
    if head == None:
        return
    
    ptr = head
    while ptr != None:
        print(f'{ptr.data}>',end=" ")
        ptr = ptr.next

def mergeTwoSortedLL(head1,head2):
    ptr1 = head1
    ptr2 = head2
    newMergedList = Node(0)
    ptr3 = newMergedList
    while True:
        if ptr1 is None:
            ptr3.next = ptr2
            break
        
        if ptr2 is None:
            ptr3.next = ptr1
            break

        if ptr1.data >= ptr2.data:
            ptr3.next = ptr2
            ptr2  = ptr2.next
        else:
            ptr3.next = ptr1
            ptr1 = ptr1.next
        
        ptr3 = ptr3.next

        
    return newMergedList.next


head:Node = None

head = insertAtHead(head,15)
head = insertAtHead(head,5)
head = insertAtPosition(head,10,1)


head2:Node = None

head2 = insertAtHead(head2,20)
head2 = insertAtHead(head2,3)
head2 = insertAtHead(head2,2)

head3 = mergeTwoSortedLL(head,head2)
printLinkedList(head3)
        