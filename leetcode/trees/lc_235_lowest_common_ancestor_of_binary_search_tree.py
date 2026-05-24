'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # we need to find the split, where
        # node.val is between p and q
        # or equal to 1 of p or q
        # we will use iterative dfs for this
        # set the current pointer to point to the root node
        current = root

        # loop as long as we have not traversed the entire tree
        # where the current node is empty
        while current:
            # if both p and q are greater than the current node
            # check the right subtree
            if p.val > current.val and q.val > current.val:
                current = current.right
            # else if both p and q are less than the current node
            # check the left subtree
            elif p.val < current.val and q.val < current.val:
                current = current.left
            # otherwise the current node is
            # between or equal to one of p and q
            # so return that current node
            # because it is the parent
            else:
                return current
