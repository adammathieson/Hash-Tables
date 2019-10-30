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
        # hash_value = 5381

        # for char in key:
        #     hash_value = ((hash_value << 5) + hash_value) + char
        # return hash_value
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        index = self._hash_mod(key)
        current = self.storage[index]
        # print("current---->", current)
        # print("storage++++>", self.storage)
        if current == None:
            # print("Index --- [][][][][] --->", index)
            self.storage[index] = LinkedPair(key, value)
            # for i in index:
            #     print('////////////in the index: ', i)
        elif current.next is None:
            current.next = LinkedPair(key, value)
            # prev = current
            # pr
            # print("This object has a next attr: ", current.next, current.next.key)
        else:
            while current.next is not None:
                if current.next.key == key:
                    print(f"Replaceing value of key {key} with {value}")
                    current.next.value = value
                    return
                else:
                    current = current.next
            current.next = LinkedPair(key, value)
            # print("added another LinkedPair to end of linked list: ", current.next.key)

        # elif current.next.key == key:
        #     print("ERROR: key is already in storage!")
        # else:
        #     for i, kv in enumerate(self.storage[index]):
        #         print("iiiiiiiiiiiii", i)
        #     print("There's something there........", self.storage[index].value)


            
            # index = LinkedPair(key, value)
            # self.storage.append(index)
            # print("Appended storage with index of: ", index.value)

        # for i, kv in slot.list():
        #     k, v = kv
        #     if k == key:
        #         print("key exists>>>>>>>>>>", k, key)
        #     else:
        #         slot.append((key, value))
            # print("Here =====>", kv)

        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        pass



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        pass


    def retrieve(self, key):
        index = self._hash_mod(key)
        current = self.storage[index]
        if current == None:
            print('Printing None')
            return None
        else:
            while current.next is not None:
                if current.key == key:
                    print("Value from retrieve: ", current.value)
                    return current.value
                else:
                    current = current.next
            return current.value
        
        # return self.storage[index].value
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        pass


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pass



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
