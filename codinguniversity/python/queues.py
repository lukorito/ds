# Implementation using singly linked list with tail
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.value

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __str__(self):
        val = []
        curr = self.head
        while curr:
            val.append(curr.value)
            curr = curr.next
        return str(val)

    def enqueue(self, val):
        node = Node(val)
        if not self.head and not self.tail:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        return self.head

    def dequeue(self):
        if not self.head:
            return None
        val = self.head
        self.head = self.head.next
        if self.head == None:
            self.tail == self.head
        return val
    
    def empty(self):
        return self.head == None

class QueueWithCircularArray:
    def __init__(self, total):
        # set array to fixed size
        self.arr = [None] * total
        self.length = len(self.arr)
        self.read_index = 0
        self.write_index = 0
    
    def __str__(self):
        return str([x for x in self.arr])


    def enqueue(self, value):
        if self.read_index == (self.write_index + 1) % self.length:
            # must leave one buffer empty
            return None
        self.arr[self.write_index] = value
        self.write_index = (self.write_index + 1) % self.length
        return self.arr

    def dequeue(self):
        if self.read_index == self.write_index:
            # queue is empty
            return None
       item = self.arr[self.read_index]
       self.arr[self.read_index] = None
       read = self.read_index = (self.read_index + 1) % self.length

    def empty(self):
        return self.read_index == self.write_index

    def full(self):
        return self.read_index == (self.write_index + 1) % self.length
        
            
            







# queue = Queue()
# print(queue)
# queue.enqueue(5)
# queue.enqueue(6)
# queue.enqueue(7)
# queue.enqueue(8)
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.empty())
# print(queue.dequeue())
# print(queue.empty())

queue = QueueWithCircularArray(3)
queue.enqueue(5)
queue.enqueue(4)
queue.enqueue(3)
queue.dequeue()
queue.enqueue(3)
print(queue)

    
