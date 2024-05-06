class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class SLL:
    def __init__(self):
        self.head = None
        
    def list_print(self):
        printval = self.head
        print("Linked List : " )
        while printval is not None:
            print(printval.data)
            printval = printval.next
    
    def search(self, x):
        Count = 0
        current = self.head
        
        while current != None:
            if current.data == x:
                print('Element is Found')
                Count = Count + 1
            current = current.next
            
        if Count == 0:
           print('Element Not Found')     
           
l1 = SLL()
l1.head = Node('30')
e2 = Node('123')
e3 = Node('345')

l1.head.next = e2
e2.next = e3
l1.list_print()

Element ='123'

print("Element to be search is : ", Element)

l1.search(Element)