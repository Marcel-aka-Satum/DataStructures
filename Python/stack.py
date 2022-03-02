#Stacks

# LIFO (last in first out)
# Push, Pop, Peek, Clear Methods
# Used in command stack (ctrl z)

#Implementation in Python using lists
my_stack = list()
my_stack.append(4)
my_stack.append(5)
my_stack.append(6)
print(my_stack)
print(my_stack.pop())
print(my_stack)

#Stack using List with a Wrapper Class
class Stack():
    def __init__(self):
        self.stack = list()
        
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return None

    def clear(self):
        if len(self.stack) > 0:
            self.stack.clear()

    def __str__(self):
        return str(self.stack)
    
