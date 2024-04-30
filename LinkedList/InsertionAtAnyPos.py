class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class SLL:
    def __init__(self):
        self.head = None
        
    def listprint(self):
        printval = self.head
        while printval is not None:
            print(printval.data)
            printval = printval.next
            
    def InsertAtAnyPos(self, nodeatpos, newdata):
        if nodeatpos is None:
            print("The node is absent.")
            return
        Newdata = Node(newdata)
        Newdata.next = nodeatpos.next
        nodeatpos.next = Newdata
        
l1 = SLL()
l1.head = Node('123')
l2 = Node('24')
l3 = Node('456')

l1.head.next = l2
l2.next = l3

l1.InsertAtAnyPos(l2, '222')
l1.listprint()