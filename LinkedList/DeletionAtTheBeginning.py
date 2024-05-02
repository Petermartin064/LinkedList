from typing import Optional
class Node:
    def __init__(self, data: int, next: Optional['Node'] = None):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        
    def print_list(self):
        printval = self.head
        print("\n[", end="")
        while printval:
            print(f' {printval.data} ', end="")
            printval = printval.next
        print(" ]")
        
    def insert_at_the_beginning(self, data: int):
        lk = Node(data)
        lk.next = self.head
        self.head = lk
        
    def delete_at_the_beginning(self):
        self.head = self.head.next     
        
if __name__ == '__main__':
    l1 = SLL()
    l1.insert_at_the_beginning(24)
    l1.insert_at_the_beginning(36)
    l1.insert_at_the_beginning(44)
    l1.insert_at_the_beginning(56)
    l1.insert_at_the_beginning(78)
    
    print('Linked List: ', end="")
    l1.print_list()
    l1.delete_at_the_beginning()
    print('Linked List after deletion: ', end="")
    l1.print_list()    