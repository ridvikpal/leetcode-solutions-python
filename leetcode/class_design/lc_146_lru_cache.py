from collections import deque


'''
https://leetcode.com/problems/lru-cache/description/
'''
class LRUCache:

    def __init__(self, capacity: int):
        # create a dictionary (hashmap)
        # for quick key-value pair lookup
        self.dictionary = dict()
        # create a deque (effectively doubly linked list)
        # to keep track of order of cache usage
        # most used to the right of queue
        # least used to the left of queue
        self.queue = deque(maxlen=capacity)
        # store the current capacity of the lru cache
        self.capacity = capacity

    def get(self, key: int) -> int:
        # first check if they key already exists
        if key in self.dictionary:
            # if it does, first update it's order
            # by moving it to the rightmost of queue
            # because it is the most recently used
            self.queue.remove(key)
            self.queue.append(key)
            # then return it's value
            return self.dictionary[key]
        # otherwise, return -1 if key doesn't exist
        # in the dictionary
        return -1

    def put(self, key: int, value: int) -> None:
        # first check if the key already exists
        if key in self.dictionary:
            # if it does, update it's value
            self.dictionary[key] = value
            # and update it's order by
            # moving it to the rightmost of queue
            # because it is the most recently used
            self.queue.remove(key)
            self.queue.append(key)
        # else the key doesn't exist in our dictionary
        else:
            # first check if we are at capacity
            if len(self.queue) == self.capacity:
                # if we are at capacity
                # remove the least recently used element
                # from the queue
                lru_key = self.queue.popleft()
                # and the dictionary
                del self.dictionary[lru_key]
            # then add the new key value to the dictionary
            self.dictionary[key] = value
            # and add the new key value to the queue
            self.queue.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
