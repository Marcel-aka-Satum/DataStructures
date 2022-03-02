#Doubly linked list Python
#PUBLIC: append, prepend, print_list, delete

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)

            itr = self.head
            while itr.next is not None:
                itr = itr.next
            itr.next = new_node
            new_node.prev = itr
            new_node.next = None 

    
    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            new_node.prev = None
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            new_node.prev = None
            self.head = new_node
        
    def print_list(self):
        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next

    def delete(self, key):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                 #case 1
                 if cur.next is None:
                     cur = None
                     self.head = None
                     return
                #case 2
                 else:
                     nxt = cur.next
                     cur.next = None
                     nxt.prev = None
                     cur = None
                     self.head = nxt
                     return
            #case 3
            elif cur.data == key:
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                #case 4
                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next

