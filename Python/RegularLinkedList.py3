#Implementation of Singly/Regular Linked List in Python
#PUBLIC: Print_list, Append, Prepend, Delete_Node, Delete_at_index

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        last_element = self.head
        while last_element:
            print(last_element.data)
            last_element = last_element.next    

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        itr = self.head
        while itr.next:
            itr = itr.next  
        itr.next = Node(data)

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):

        cur_node = self.head

        if cur_node and cur_node.next == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev_node = None
        while cur_node and cur_node.data != key:
            prev_node = cur_node
            cur_node = cur_node.next
        
        if cur_node is None:
            return
        
        prev_node.next = cur_node.next
        cur_node = None
    
    def delete_at_index(self, index):

        cur_node = self.head

        if index == 0:
            self.head = cur_node.next
            cur_node = None
            return

        counter = 0
        prev_node = None
        while cur_node and counter < index:
            prev_node = cur_node
            cur_node = cur_node.next
            counter += 1

        if cur_node is None:
            raise Exception('The index is greater than elements in the list')
        prev_node.next = cur_node.next
        cur_node = None 

