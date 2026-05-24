from typing import Optional


'''
https://leetcode.com/problems/invert-binary-tree/description/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # our recursive base case is when
        # we reach a node that is None
        if not root:
            # in that case, just return directly
            return
        
        # recursively reverse left subtree
        root.left = self.invertTree(root.left)
        # recursively reverse right subtree
        root.right = self.invertTree(root.right)

        # swap the left and right subtrees for the current node
        root.left, root.right = root.right, root.left

        # return the swapped node
        return root
