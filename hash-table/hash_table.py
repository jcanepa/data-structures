# Hashtable -
# An unordered key-value data structure that provides
# O(1) store, retrieve search and delete operations.
#
# @author Julian Canepa
# @date   6 October 2021

class HashTable:

    def __init__(self, size=20):
        self.size = size
        self.data = [[] for i in range(size)]

    def __setitem__(self, key, value):
        index = self.hash(key)
        slot = self.data[index]

        # Examine existing elements at the slot
        for i in range(len(slot)):
            # If key is already set, remove it
            if slot[i][0] == key:
                del slot[i]
                break
        slot.append([key, value])

    def __getitem__(self, key):
        index = self.hash(key)
        slot = self.data[index]

        for i in range(len(slot)):
            if key == slot[i][0]:
                return slot[i][1]

    def delete(self, key):
        index = self.hash(key)
        slot = self.data[index]

        for i in range(len(slot)):
            if key == slot[i][0]:
                del slot[i]
                return

    def clear(self):
        self.data = [[] for i in range(self.size)]

    def keys(self):
        keys = []
        for slot in self.data:
            for i in range(len(slot)):
                keys.append(slot[i][0])
        return keys

    def values(self):
        values = []
        for slot in self.data:
            for i in range(len(slot)):
                values.append(slot[i][1])
        return values

    def hash(self, key):
        return hash(key) % self.size
