from typing import Optional


'''
https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # create an array to hold our in order
        # traversal of the bst
        in_order_path = []

        # create our dfs function to traverse the bst in order
        def dfs(root):
            # our base case is when we reach node = None
            if not root:
                # just return
                return

            # traverse left subtree
            dfs(root.left)

            # add current value to the in order path array
            in_order_path.append(root.val)
            
            # traverse right subtree
            dfs(root.right)

        # run our dfs starting on root node
        dfs(root)

        # in order path is sorted smallest to largest
        # just return the index-1 (because index starts at 0)
        # for the k smallest value
        return in_order_path[k-1]
