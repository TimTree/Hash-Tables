# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        theHash = self._hash_mod(key)  # the hash represents location index of storage
        keyValuePairs = self.storage[theHash]
        if keyValuePairs is not None:
            while keyValuePairs.next is not None:
                if keyValuePairs.key == key:
                    keyValuePairs.value = value
                    print(f"Overwritten key {key} with {value}, hash number {theHash}")
                    return
                keyValuePairs = keyValuePairs.next
            if keyValuePairs.key == key:
                keyValuePairs.value = value
                print(f"Overwritten key {key} with {value}, hash number {theHash}")
                return
            keyValuePairs.next = LinkedPair(key, value)
            print(f"Added {key}, {value}, hash number {theHash}")
        else:
            self.storage[theHash] = LinkedPair(key, value)
            print(f"Added {key}, {value}, hash number {theHash}")

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''

        theHash = self._hash_mod(key)  # the hash represents location index of storage
        keyValuePairs = self.storage[theHash]

        if keyValuePairs is not None:
            if keyValuePairs.key == key: # If key to remove is first in linkedpair
                self.storage[theHash] = keyValuePairs.next
                print(f"Deleted key {key}")
            else:
                while keyValuePairs.next is not None:
                    if keyValuePairs.next.key == key:
                        keyValuePairs.next = keyValuePairs.next.next
                        print(f"Deleted key {key}")
                        break
                    keyValuePairs = keyValuePairs.next
        else:
            print(f"Key {key} not found")

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        theHash = self._hash_mod(key)  # the hash represents location index of storage
        keyValuePairs = self.storage[theHash]

        if keyValuePairs is not None:
            while keyValuePairs.next is not None:
                if keyValuePairs.key == key:
                    return keyValuePairs.value
                keyValuePairs = keyValuePairs.next
            if keyValuePairs.key == key:
                return keyValuePairs.value
            else:
                return None
        else:
            return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        oldStorage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity
        print('')
        for keyValuePairs in oldStorage:
            while keyValuePairs is not None:
                self.insert(keyValuePairs.key, keyValuePairs.value)
                keyValuePairs = keyValuePairs.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
