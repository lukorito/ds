# Linked list uses pointer in the next value 
# the head offers a pointer to the next node and so forth.
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
