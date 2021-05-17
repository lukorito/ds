import queue

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
        #DFS
        # inorder gives a sorted list
        '''
        Time complexity O(n)
        Space complexity : O(h)
        '''
        arr = []
        def dfs(head):
            if not head:
                return            
            dfs(head.left)   
            arr.append(head.val)         
            dfs(head.right) 

        dfs(self.head)
        return str(arr)

    # def  get_height(self):

    def bfs(self):
        '''
        Time complexity O(n)
        Space complexity : best O(1) worst O(n/2)
        '''
        if not self.head:
            return None
        arr = []
        q = queue.Queue()
        q.put(self.head)
        while not q.empty():
            curr = q.get()
            arr.append(curr.val)
            if curr.left:
                q.put(curr.left)
            if curr.right:
                q.put(curr.right)
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

    def find_height(self):
        def height(node):
            if not node:
                return -1
            return max(height(node.left), height(node.right)) + 1
        return height(self.head)

    def is_binary_search_tree(self):
        '''
        Time Complexity O(n)
        '''
        def helper(node, minVal, maxVal):
            # data has to always be within the range of mix and max
            if not node:
                return True
            if (node.val > minVal and node.val < maxVal
            and helper(node.left, minVal, node.val)
            and helper(node.right, node.val, maxVal)
            ):
                return True
            else:
                return False
        return helper(self.head, float('-inf'), float('inf'))
        


                

bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(4)
bst.insert(6)
print(bst.is_binary_search_tree())