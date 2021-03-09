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

    def __str__(self):
       return  str(self.__repr__())

    def __repr__(self):
        arr = []
        curr = self.head
        while curr:
            arr.append(curr.value)
            curr = curr.next
        return arr

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
        
    def insert(self, index, value):
        new_node = Node(value)
        if index > self.size+1:
            return None
        if self.head == None:
            self.head = new_node
            self.size+=1
            return self.head
        curr = self.head
        count = 0
        while curr:    
            if index == count:
                next_pointer = curr.next
                new_node.next = next_pointer                
                curr.next = new_node
                self.size+=1
                return self.head
            curr = curr.next
            count += 1

    def erase(self, index):
        if index > self.size:
            return None
        curr = self.head
        prev = None
        count = 0
        while curr:
            if index == count:
                next_pointer = curr.next
                prev.next = next_pointer
                return self.head
            prev = curr
            curr = curr.next
            count += 1


    def value_n_from_end(self, n):
        position = self.size - (n + 1)
        count = 0
        curr = self.head
        while curr:
            if count == position:
                return curr.value
            count+=1
            curr = curr.next
        pass

    def reverse(self):
        if not self.head:
            return None
        if self.size == 1:
            return self.head
        curr = self.head
        prev = None
        while curr:
            next_pointer = curr.next
            curr.next = prev
            prev = curr
            curr = next_pointer
        return prev


    def remove_value(value):
        curr = self.head
        prev = None
        while curr:
            if curr.value == value:
                next_pointer = curr.next
                prev.next = next_pointer
                return self.head
            prev = curr
            curr = curr.next






def main():
    list = LinkedList()
    list.insert(0, 1)
    list.insert(0, 4)
    list.insert(1, 5)
    list.insert(2, 6)
    # list.erase(1)
    print(list.reverse())
    # print(list)
    # print(list.value_n_from_end(2))
    # print(list.front())
    
    # print(list.value_at(6))

if __name__ == '__main__':
    main()