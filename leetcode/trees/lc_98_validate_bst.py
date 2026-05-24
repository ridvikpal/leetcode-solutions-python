import math
from typing import Optional


'''
https://leetcode.com/problems/validate-binary-search-tree/description/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # our dfs function to search the entire tree
        def dfs(root, lower_bound, upper_bound):
            # our base case, if we reach a leaf node
            # return true because leaf nodes are by default ok
            if not root:
                return True

            # if our value is not in the bound, return False
            if not lower_bound < root.val < upper_bound:
                return False

            # run dfs on left subtree
            # note left node should be smaller than root node
            # so set upper bound to root node
            left_ok = dfs(root.left, lower_bound, root.val)

            # run dfs on right subtree
            # note right node should be larger than root node
            # so set lower bound to root node
            right_ok = dfs(root.right, root.val, upper_bound)

            # only if left and right subtrees are valid return True
            # else return False
            return left_ok and right_ok

        # we can run our dfs with initial bounds [-inf, inf]
        return dfs(root, -math.inf, math.inf)
