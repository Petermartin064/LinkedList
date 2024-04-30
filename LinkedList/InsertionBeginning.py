class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class SLL:
    def __init__(self):
        self.head = None
        
    def listprint(self):
        printval =self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next
            
    def AddAtBeginning(self, newdata):
        NewNode = Node(newdata)
        NewNode.next = self.head
        self.head = NewNode

l1 = SLL()
l1.head = Node('123')
e2 = Node('456')
e3 = Node('789')

l1.head.next = e2
e2.next = e3

l1.AddAtBeginning('222')
l1.listprint()