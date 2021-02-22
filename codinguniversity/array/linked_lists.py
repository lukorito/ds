# Linked list uses pointer in the next value 
# the head offers a pointer to the next node and so forth.
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.value
        
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

    def push_front(self,value):
        new_node = Node(value)
        curr = self.head
        if not curr:
            self.head = new_node
        new_node.next = curr
        self.head = new_node
        return self.head
        
    def pop_front(self):
        curr = self.head
        if not curr:
            return None
        if not curr.next:
            self.head = None
            return curr.value
        self.head = curr.next
        return curr.value
    
    def pop_back(self):
        curr = self.head
        prev = curr
        while curr:
            if not curr.next:
                prev.next = None
                return curr.value
            prev = curr
            curr = curr.next
    
    def front(self):
        if self.head:
            return self.head.value
    
    def back(self):
        curr = self.head
        while curr:
            if not curr.next:
                return curr.value
            curr = curr.next
        
    # def insert(self, index, value):
    #     new_node = Node(value)
    #     curr = self.head
    #     if not curr or index == 0:
    #         next_item = curr.next
    #         new_node.next = next_item
    #         self.head = new_node
    #     while curr and index > 0:
    #         curr = curr.next
    #         index-=1
    #     if index == 0:
    #         next_item = curr.next
    #         new_node.next = next_item
    #         curr.next = new_node

    def erase(self, index):
        pass

    def value_n_from_end(self, n):
        pass

    def reverse(self):
        pass

    def remove_value(value):
        pass





def main():
    list = LinkedList()
    list.insert(0, 1)
    print(list.front())
    
    # print(list.value_at(6))

if __name__ == '__main__':
    main()