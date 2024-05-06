class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
    
    def listprint(self):
        printval = self.head
        print('Linked list')
        while printval is not None:
            print(printval.data)
            printval = printval.next

    def reverse(self):
        prev = None
        curr = self.head
        while(curr is not None):
            Next = curr.next
            curr.next = prev
            prev = curr
            curr = Next
        self.head = prev
        
l1 = SLL()
l1.head = Node('731')
e2 = Node('111')
e3 = Node('234')

l1.head.next = e2
e2.next = e3

l1.listprint()
l1.reverse()
print('After reversing : ')
l1.listprint()
    