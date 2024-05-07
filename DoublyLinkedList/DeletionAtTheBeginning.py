class Node:
    def __init__(self, data, key):
        self.data = data
        self.key = key
        self.next = None
        self.prev = None
        
head = None
last = None
current = None

def is_Empty():
    return head == None

def print_list():
    ptr = head
    while ptr != None:
        print(f"({ptr.key}, {ptr.data})", end=" ")
        ptr = ptr.next

def insert_first(key, data):
    global head, last
    
    link = Node(key, data)
    
    if is_Empty():
        last = link
    else:
        head.prev = link
        link.next = head
    head = link
    
def delete_first():
    global head, last
    
    if is_Empty():
        print('There is nothing to delete')
        return
    tempLink = head
    
    if head.next == None:
        last = None
    else:
        head.next.prev = None
    head = head.next

insert_first(1, 10)
insert_first(2, 20)
insert_first(3, 30)
insert_first(4, 40)
print("List before deletion : ",)
print_list()
print("\nList after deletion : ")
delete_first()
print_list()