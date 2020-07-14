class ListNode:
    '''
    Each ListNode holds a reference to its previous node
    as well as its next node in the List.
    '''
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    
    def insert_after(self, value):
        '''
        Wrap the given value in a ListNode and insert it
        after this node.
        '''
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next
    
    def insert_before(self, value):
        '''
        Wrap the given value in a ListNode and insert it
        before this node.
        '''
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

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
         # if list is empty
        if self.head is None:
            node = ListNode(value)
            self.head = node
            self.tail = node
        else:
            # use node insert before and update pointers
            self.head.insert_before(value)
            self.head = self.head.prev
        self.length += 1
        
    def remove_from_head(self):
        '''
        Removes the List's current head node, making the
        current head's next node the new head of the List.
        Returns the value of the removed Node.
        '''
        return self.delete(self.head)
            
    def add_to_tail(self, value):
        '''
        Wraps the given value in a ListNode and inserts it 
        as the new tail of the list. Don't forget to handle 
        the old tail node's next pointer accordingly.
        '''
        # list is empty
        if self.tail is None:
            node = ListNode(value)
            self.head = node
            self.tail = node
        else:
            # use node insert after and update pointers
            self.tail.insert_after(value)
            self.tail = self.tail.next
        self.length += 1
            
    def remove_from_tail(self):
        '''
        Removes the List's current tail node, making the 
        current tail's previous node the new tail of the List.
        Returns the value of the removed Node.
        '''
        return self.delete(self.tail)
            
    def move_to_front(self, node):
        '''
        Removes the input node from its current spot in the 
        List and inserts it as the new head node of the List.
        '''
        self.delete(node)
        self.add_to_head(node.value)
        
    def move_to_end(self, node):
        '''
        Removes the input node from its current spot in the 
        List and inserts it as the new tail node of the List.
        '''
        self.delete(node)
        self.add_to_tail(node.value)

    
    def delete(self, node):
        '''
        Deletes the input node from the List, preserving the 
        order of the other elements of the List.
        '''
        # if no nodes
        if self.head is None:
            return None
        # if only node
        elif node == self.head and node == self.tail:
            self.head = None
            self.tail = None
        # if node is head
        elif node == self.head:
            self.head.delete()
            self.head = self.head.next
        # if node is tail
        elif node == self.tail:
            self.tail.delete()
            self.tail = self.tail.prev
        # node in middle of list
        else:
            node.delete()
        # because only the no nodes if returns, I can put this here
        # to cover decrementing the length for all other cases
        self.length -= 1
        return node.value

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        cur = self.head
        maxval = 0
        if cur is None:
            return None
        while True:
            # Update value if larger
            if maxval < cur.value:
                maxval = cur.value

            # break infinite loop
            if cur.next is None:
                break

            cur = cur.next
        return maxval