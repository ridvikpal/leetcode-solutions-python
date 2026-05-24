from typing import Optional


'''
https://leetcode.com/problems/copy-list-with-random-pointer/description/
'''
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # handle the edge case if we are 
        # given an empty linked list
        if not head:
            # just return None
            return None

        # first setup a dictionary to map old nodes
        # to new deep copied nodes that we create
        oldToNew = dict()

        # first pass
        # loop through linked list
        # create deep copies and store them in hashmap
        # do not link them together
        current = head
        while current:
            copy = Node(current.val)
            oldToNew[current] = copy
            current = current.next

        # second pass
        # loop through linked list again
        # link next and random pointers
        # by looking up in hashmap created
        # in first pass
        current = head
        while current:
            current_copy = oldToNew[current]
            # only create next link if it exists
            if current.next:
                current_copy.next = oldToNew[current.next]
            # only create random link if it exists
            if current.random:
                current_copy.random = oldToNew[current.random]
            current = current.next

        # return the new head by looking it up in the dict
        return oldToNew[head]
