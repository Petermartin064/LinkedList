from typing import Optional
class Node:
    def __init__(self, data: int, next: Optional['Node'] = None ):
        self.data = data
        self.next = None
        
class SLL:
    def __init__(self):
        self.head = None
        
    def listprint(self):
        printval = self.head
        print("\n[", end="")
        while(printval != None):
            print(" ", printval.data, " ", end="")
            printval = printval.next
        print(']')
            
    def insert_at_the_beginning(self, data):
        lK = Node(data)
        lK.next = self.head
        self.head = lK
    
    def deletenode(self, key):
        temp = self.head
        
        if(temp != None and temp.data == key):
            self.head = temp.next
            return
        
        while(temp != None and temp.data != key):
            prev = temp
            temp = temp.next
            
        if (temp == None):
            return
        prev.next = temp.next
        
l1 = SLL()
l1.insert_at_the_beginning(10)
l1.insert_at_the_beginning(20)
l1.insert_at_the_beginning(30)
l1.insert_at_the_beginning(40)
l1.insert_at_the_beginning(50)
l1.insert_at_the_beginning(60)
print("Original Linked List: ", end="")

l1.listprint()
l1.deletenode(30)
print('Linked List After Deletion: ', end="")

l1.listprint()