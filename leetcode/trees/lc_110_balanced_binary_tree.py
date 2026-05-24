from typing import Optional


'''
https://leetcode.com/problems/balanced-binary-tree/description/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # init our result to be true
        # we assume the binary tree is balanced to begin with
        self.result = True

        # our recursive dfs function to compute the
        # height of the tree
        def calculate_height(node) -> int:
            # our base case is if
            # 1) we are given an empty leaf node
            # 2) we've already found out the tree isn't balanced
            if not node or not self.result:
                # in that case automatically return 0
                return 0

            # compute the left subtree height
            left_height = calculate_height(node.left)
            # compute the right subtree height
            right_height = calculate_height(node.right)

            # if the difference between left and right subtree height
            # is greater than 1
            if abs(left_height-right_height) > 1:
                # then our result should be set to false
                self.result = False

            # finally we can return the max height between subtrees + 1
            return max(left_height, right_height) + 1

        # compute the height of the entire tree
        calculate_height(root)

        # finally return verdict on whether the binary tree is balanced
        return self.result
