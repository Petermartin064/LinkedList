class Node:
    def __init__(self, data, key):
        self.data = data
        self.key = key
        self.prev = None
        self.next = None
        
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

def insert_at_the_beginning(key, data):
    global head, last
    
    link = Node(key, data)
    if is_empty():
        last = link
    else:
        head.prev = link
    link.next = head
    head = link

insert_at_the_beginning(1, 10)
insert_at_the_beginning(2, 20)
insert_at_the_beginning(3, 30)
insert_at_the_beginning(4, 40)
insert_at_the_beginning(5, 50)

print('Doubly Linked List : ')

print_list()