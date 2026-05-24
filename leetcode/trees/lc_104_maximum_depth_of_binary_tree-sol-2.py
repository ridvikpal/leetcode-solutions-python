from typing import Optional


'''
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # we will use a recursive dfs solution to solve this problem
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if we are at an empty leaf node
        if not root:
            # return 0
            # there is no depth at this level
            # because there are no nodes at this level
            return 0

        # otherwise, recursively dfs search on left subtree
        max_left = self.maxDepth(root.left)
        # recursively dfs search on right subtree
        max_right = self.maxDepth(root.right)

        # return the max between the left and right subtrees
        # plus 1 because there is a node on this current level
        return max(max_left, max_right)+1
