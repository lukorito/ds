# Implement a vector (mutable array with automatic resizing):
# Python list has dynamic arrays
import sys

class Array:
    def __init__(self):
        self.array = []

    def size(self) -> int:
        return len(self.array)

    def capacity(self) -> int:
        return sys.getsizeof(self.array) // 8 # // discards the fractional part

    def is_empty(self) -> bool:
        return len(self.array) == 0
    
    def at(self,i: int) -> any:
        try:
            return self.array[i]
        except IndexError:
            return None
    def push(self, item):
        return self.array.append(item)
    
    def insert(self, index:int, item):
        return self.array.insert(index, item)
    
    def prepend(self, item):
        return self.array.insert(0, item)

    def pop(self, item):
        return self.array.pop()

    def delete(self, index: int):
        return self.array.pop(index)

    def remove(self, item):
        return [x for x in self.array if x != item]

    def find(self, item):
        try:
            return self.array.index(item)
        except ValueError:
            return -1


if __name__ == '__main__': #
    new_array = Array()
    print(new_array.at(1))
    print(new_array.capacity())
    new_array.push(5)
    new_array.push(9)
    new_array.push(3)
    print(new_array.find(10))