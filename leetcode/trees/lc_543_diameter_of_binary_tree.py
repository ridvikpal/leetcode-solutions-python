from typing import Optional


'''
https://leetcode.com/problems/diameter-of-binary-tree/description/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # the diameter of a binary tree is essentially the sum of the
    # max left subtree height and the max right subtree height
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # init our tree's diameter
        self.diameter = 0

        # our recursive dfs function to compute the height of a tree
        def calculate_height(node) -> int:
            # our base case is if we are given an empty leaf node
            if not node:
                # the height in this case is 0 so return it
                return 0

            # compute the left subtree height
            left_subtree_height = calculate_height(node.left)
            # compute the right subtree height
            right_subtree_height = calculate_height(node.right)

            # update the diameter with the sum of
            # left and right subtree height if required
            self.diameter = max(self.diameter, left_subtree_height+right_subtree_height)

            # return the max of the left or right subtree + 1
            # to compute the height of the tree
            return max(left_subtree_height, right_subtree_height) + 1

        # we will call our calculate_height function with the root node
        calculate_height(root)

        # finally, return the diameter we computed
        return self.diameter
