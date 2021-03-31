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
        self.count = 0
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        #hashes the table
        return int(key) % self.size

    def set(self, key, value):
        #adds a key to the table
        hash_value = self._hash_function(key)
        for item in self.table[hash_value]:
            if item.key == key:
                item.value = value
                return 
        self.table[hash_value].append(Item(key, value))
        self.count+=1

    def get(self, key):
        #gets a key from the table
        hash_value = self._hash_function(key)
        for item in self.table[hash_value]:
            if item.key == key:
                return item
        raise KeyError("Key not found")

    def remove(self, key):
        #removes a key from the table
        hash_value = self._hash_function(key)
        for index, item in enumerate(self.table[hash_value]):
            if item.key == key:
                del self.table[hash_value][index]
                return item
        raise KeyError("Key not found")

    def empty(self):
        # checks if the table is empty
        return self.count == 0

    def exists(self, key):
        #checks if a key exists
        hash_value = self._hash_function(key)
        for item in self.table[hash_value]:
            if item.key == key:
                return True
        return False
    

hashtable = HashTable(5)
hashtable.set(3, "Kelvin")
print(hashtable.get(3))

            