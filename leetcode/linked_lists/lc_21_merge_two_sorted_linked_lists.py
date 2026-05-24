from typing import Optional


'''
https://leetcode.com/problems/merge-two-sorted-lists/description/
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # first init a dummyHead
        # and head variable
        # as new ListNodes
        dummyHead = head = ListNode()

        # loop as long as we have both
        # a list1 and list2 pointer
        # that are not None
        # i.e. loop until we have
        # fully traversed one of the lists
        while list1 and list2:
            # if the current list1 node 
            # is smaller than the
            # current list2 node
            if list1.val < list2.val:
                # then set the next head value
                # to point to list1
                head.next = list1
                # and increment list1 to point
                # to the next list1 node
                list1 = list1.next
            # else the current list2 node
            # is larger than or equal to
            # the current list1 node
            else:
                # then set the next head value
                # to point to list2
                head.next = list2
                # and increment list2 to point
                # to the next list2 node
                list2 = list2.next

            # always increment head to point
            # to the next head node at the
            # end of every iteration
            head = head.next

        # now check if we still have list1
        # to traverse
        if list1:
            # if we do, set head.next
            # to point to the remaining
            # list1 nodes
            head.next = list1
        # else check if we still have list2
        # to traverse
        elif list2:
            # if we do, set head.next
            # to point to the remaining
            # list2 nodes
            head.next = list2

        # finally return dummyHead.next
        # which always points to the actual head
        return dummyHead.next
