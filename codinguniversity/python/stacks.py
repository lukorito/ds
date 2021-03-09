class Stack:
    def __init__(self):
        self.collection = []

    def empty(self):
        return len(self.collection) > 0

    def top(self):
        return self.collection[0]

    def pop(self):
        return self.collection.pop(0)
    
    def insert(self, value):
        return self.collection.insert(0, value)

def main():
    new_stack = Stack()
    new_stack.insert(1)
    new_stack.insert(2)
    new_stack.insert(3)
    print(new_stack.collection)


if __name__ == '__main__':
    main()