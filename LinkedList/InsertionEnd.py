class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLL:
    def __init__self(self):
        self.head = None
        
    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next
            
l1 = SLL()
l1.head = Node('123')
l2 = Node('12')
l3 = Node('456')
l4 = Node('789')

l1.head.next = l2
l2.next = l3
l3.next = l4

l1.listprint()