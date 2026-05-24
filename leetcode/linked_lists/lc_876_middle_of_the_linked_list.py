from typing import Optional


'''
https://leetcode.com/problems/middle-of-the-linked-list/description/
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # we will use a fast and slow pointer
        # the fast pointer will go at double the speed
        # as the slow pointer
        # init our fast and slow pointers to the head
        fast = slow = head

        # loop as long as the fast pointer
        # and the fast pointer's next pointer
        # are not None
        while fast and fast.next:
            # the fast pointer moves at double the speed
            fast = fast.next.next
            # the slow pointer moves at regular speed
            slow = slow.next

        # at the end of the iteration, the slow pointer
        # must be at the middle of the linked list
        # so we can just return it
        return slow
