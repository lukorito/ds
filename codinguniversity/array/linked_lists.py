# Linked list uses pointer in the next value 
# the head offers a pointer to the next node and so forth.
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
class LinkedList: 
    def __init__(self):
        self.size = 0
        self.head = None

    def size(self):
        return self.size

    def empty(self):
        return self.head == None

    def value_at(self, index):
        if not self.head:
            return None
        curr = self.head
        count = 0
        while curr and count <= index:
            if index == count:
                return curr.value
            count+=1
            curr=curr.next

    def push_front(value):
        new_node = Node(value)
        




def main():
    list = LinkedList()
    head = Node(3)
    node1 = Node(1)
    node2 = Node(2)
    list.head = head
    head.next = node1
    head.next.next = node2
    print(list.value_at(6))

if __name__ == '__main__':
    main()