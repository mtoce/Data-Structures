class ListNode:
    def __init__(self, value, prev=None, next=None):
        '''
        Each ListNode holds a reference to its previous node
        as well as its next node in the List.
        '''
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        '''
        Rearranges this ListNode's previous and next pointers
        accordingly, effectively deleting this ListNode.
        '''
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

class DoublyLinkedList:
    '''
    Our doubly-linked list class. It holds references to 
    the list's head and tail nodes.
    '''
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
   
    def add_to_head(self, value):
        '''
        Wraps the given value in a ListNode and inserts it 
        as the new head of the list. Don't forget to handle 
        the old head node's previous pointer accordingly.
        '''
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
 
    def remove_from_head(self):
        '''
        Removes the List's current head node, making the
        current head's next node the new head of the List.
        Returns the value of the removed Node.
        '''
        value = self.head.value
        self.delete(self.head)
        return value

    def add_to_tail(self, value):
        '''
        Wraps the given value in a ListNode and inserts it 
        as the new tail of the list. Don't forget to handle 
        the old tail node's next pointer accordingly.
        '''
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.tail and not self.head:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            

    def remove_from_tail(self):
        '''
        Removes the List's current tail node, making the 
        current tail's previous node the new tail of the List.
        Returns the value of the removed Node.
        '''
        value = self.tail.value
        self.delete(self.tail)
        return value
            
    def move_to_front(self, node):
        '''
        Removes the input node from its current spot in the 
        List and inserts it as the new head node of the List.
        '''
        if node is self.head:
            return
        value = node.value
        if node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1
        self.add_to_head(value)
        
    def move_to_end(self, node):
        '''
        Removes the input node from its current spot in the 
        List and inserts it as the new tail node of the List.
        '''
        if node is self.tail:
            return
        value = node.value
        if node is self.head:
            self.remove_from_head()
            self.add_to_tail(value)
        else:
            node.delete()
            self.length -= 1
            self.add_to_tail(value)

    def delete(self, node):
        '''
        Deletes the input node from the List, preserving the 
        order of the other elements of the List.
        '''
        self.length -= 1
        if not self.head and not self.tail:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = node.next
            node.delete()
        elif self.tail == node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()

    def get_max(self):
        '''
        Finds and returns the maximum value of all the nodes 
        in the List.
        '''
        if not self.head:
            return None
        max_val = self.head.value
        current = self.head
        while current:
            if current.value > max_val:
                max_val = current.value
            current = current.next
        return max_val