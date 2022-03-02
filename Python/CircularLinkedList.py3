#Circular Linked List Python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None    

class DoubleList:
    def __init__(self):
        self.head = None
   
    def append(self, data):
        #case 1
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            new_node.next = self.head
            return
        #case 2
        else:
            new_node = Node(data)
            itr = self.head
            while itr.next != self.head:
                itr = itr.next
            itr.next = new_node
            new_node.next = self.head
            
    def prepend(self, data):
        #case 1
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            new_node.next = self.head
            return
        #case 2
        itr = self.head
        new_node = Node(data)
        while itr.next != self.head:
            itr = itr.next
        itr.next = new_node
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        if self.head is None:
            raise Exception("There are no Nodes in the list")
        itr = self.head
        while itr:
            print(itr.data)
            itr = itr.next
            if itr == self.head:
                break
    def remove(self, key):
        #key == header
        if key == self.head.data:
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = self.head.next
            self.head = self.head.next
            return
        #Empty list
        elif self.head is None:
             raise Exception("There are no Nodes in the list")
        # 1 Node
        elif self.head.next == self.head:
            current_node = self.head
            current_node.next = None
            self.head = None
            return
        else:
            current_node = self.head
            prev_node = None
            while current_node.data != key:
                prev_node = current_node
                current_node = current_node.next
            prev_node.next = current_node.next
            current_node.next = None
            current_node = None

    def remove_at_index(self, index):
        if self.head is None:
            raise Exception("There are no Nodes in the list")
        elif index == 0 and self.head.next == self.head:
            current_node = self.head
            current_node.next = None
            self.head = None
            return
        elif index == 0:
            current_node = self.head
            while current_node.next != self.head:
                current_node = current_node.next
            current_node.next = self.head.next
            self.head = self.head.next
            return
        else:
            counter = 0 
            current_node = self.head
            prev_node = None
            while counter < index and current_node.next != self.head:
                prev_node = current_node
                current_node = current_node.next
                counter += 1
            prev_node.next = current_node.next
            current_node.next = None
            current_node = None
