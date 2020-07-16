from singly_linked_list import LinkedList

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 
1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
# Part 1: Implement stack class using an array
class ArrayQueue:
    # Initialize class with size of 0 and empty stack/list
    def __init__(self):
        self.size = 0
        self.storage = []
    
    # Check length of self.storage stack/list
    def __len__(self):
        return len(self.storage)

    # Append value to the top of the stack/list
    def push(self, value):
        self.storage.append(value)

    # Deletes value from top of the stack/list, returns the value at the top of the stack
    def pop(self):
        # For pop and peek methods, check whether stack is empty, to avoid exceptions
        if len(self.storage) > 0:
            return self.storage.pop(0)
        else:
            return None

# Part 2: Re-implement stack class using a linked list
class Queue():
    # Initialize class with size of 0 and empty stack/list
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    # Check length of self.storage stack/list
    def __len__(self):
        return self.size

    # Append value to the end of the stack/list
    # def push(self, value):
    #     self.storage.add_to_tail(value)
    #     self.size += 1

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
         # If stack is empty, return nothing
        if self.size == 0:
            return None
        else:
            self.size -= 1
            return self.storage.remove_head()

    # Deletes value from end of the stack/list, returns the element at the top of the stack
    # def pop(self):
    #     # If stack is empty, return nothing
    #     if self.size == 0:
    #         return None
    #     # If stack has values, remove the last one
    #     else:
    #         self.size -= 1
    #         return self.storage.remove_tail()