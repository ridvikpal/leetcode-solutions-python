from typing import Optional


'''
https://leetcode.com/problems/linked-list-cycle/description/
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # create a visited set
        # to keep track of nodes we have visited
        visited = set()

        # loop through all nodes
        while head:
            # if we have already visited this node
            # cycle exists so return true
            if head in visited:
                return True

            # otherwise add node to visited set
            visited.add(head)
            # increment to next node in linked list
            head = head.next

        # if we eventually reach end of linked list
        # return true because there are no cycles
        return False
