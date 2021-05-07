from queues import Queue

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)

class BinarySearchTree:
    def __init__(self):
       self.head = None
    
    def __str__(self):
        # BFS
        queue = Queue()
        arr = []
        queue.enqueue(self.head)
        # print(queue)
        while not queue.empty():
            curr = queue.dequeue()
            print(curr, "curr queue")
            arr.append(curr.value)
            if curr.value.left:
                queue.enqueue(curr.value.left)
            if curr.value.right:
                queue.enqueue(curr.value.right)
        return arr   

    def insert(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            return self.head
        else:
            curr = self.head
            while curr:
                if val < curr.val:             
                    if curr.left:  
                        curr = curr.left
                    else:
                        curr.left = newNode
                        break
                else:
                    if curr.right:
                        curr = curr.right
                    else:
                        curr.right = newNode
                        break
        return self.head.left

                

bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
print(bst)