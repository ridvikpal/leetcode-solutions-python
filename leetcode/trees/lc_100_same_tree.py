from typing import Optional


'''
https://leetcode.com/problems/same-tree/description/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if both nodes are None, they're the same
        if not p and not q:
            return True

        # if any one of them are None but the other isn't
        # they are not the same
        if (not p and q) or (p and not q):
            return False

        # check each left and right subtree recursively
        left_res = self.isSameTree(p.left, q.left)
        right_res = self.isSameTree(p.right, q.right)

        # if left or right subtrees are not the same, return False
        if not left_res or not right_res:
            return False

        # finally, we can just check the values to see if they are the same.
        return p.val == q.val
