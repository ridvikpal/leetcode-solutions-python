from typing import List, Optional


'''
https://leetcode.com/problems/binary-tree-postorder-traversal/description/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # create our result array
        result = []

        # run a dfs post order traversal algorithm
        def dfs(root):
            # our base case is when we reach root = None
            if not root:
                return None

            # as per post order,
            # visit left and right subtrees first
            dfs(root.left)
            dfs(root.right)

            # then visit the root
            # and append it to our result list
            result.append(root.val)

        # perform dfs with the starting root node
        dfs(root)

        # return the result array
        return result
