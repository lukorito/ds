# assume keys are intergers
# use chaining for collision
# not to worry about load factor
# assume inputs are valid
class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __str__(self):
        return str({"key": self.key, "value" : self.value})

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return int(key) % self.size

    def set(self, key, value):
        hash_value = self._hash_function(key)
        for item in self.table[hash_value]:
            if item.key == key:
                item.value = value
                return 
        self.table[hash_value].append(Item(key, value))

    def get(self, key):
        hash_value = self._hash_function(key)
        for item in self.table[hash_value]:
            if item.key == key:
                return item
        raise KeyError("Key not found")

    def remove(self, key):
        hash_value = self._hash_function(key)
        for index, item in enumerate(self.table[hash_value]):
            if item.key == key:
                del self.table[hash_value][index]
                return item
        raise KeyError("Key not found")

hashtable = HashTable(5)
hashtable.set(3, "Kelvin")
print(hashtable.get(3))

            