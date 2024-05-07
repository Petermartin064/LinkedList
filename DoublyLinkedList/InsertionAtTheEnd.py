class Node:
    def __init__(self, data, key):
        self.data = data
        self.key = key
        self.next = None
        self.prev = None
        
head = None
last = None
current = None

def is_empty():
    return head == None
def print_list():
    ptr = head
    while ptr != None:
        print(f"({ptr.key}, {ptr.data})", end=" ")
        ptr = ptr.next
        
def insert_at_the_beginnig(key, data):
    global head, last
    
    link = Node(key, data)
    
    if is_empty():
        last = link
    else:
        head.prev = link
    link.next = head
    head = link
    
def insert_last(key, data):
    global head, last
    
    link = Node(key, data)
    
    if is_empty():
        last = link
    else:
        last.next = link
        link.prev = last
    last = link

insert_at_the_beginnig(1, 10)
insert_at_the_beginnig(2, 20)
insert_at_the_beginnig(3, 30)
insert_last(4, 40)

print("Doubly Linked List : ", end="")
print_list()