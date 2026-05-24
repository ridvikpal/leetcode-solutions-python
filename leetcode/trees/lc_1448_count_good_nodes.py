'''
https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # init our count of good nodes
        self.count = 0
        
        # our dfs function used to traverse the tree pre-order
        def dfs(root, max_value):
            # our base case is when we reach a None root
            if not root:
                # just return because we have completed a full path
                return

            # if the root value is >= the max value so far
            # increment the count
            if root.val >= max_value:
                max_value = root.val
                self.count += 1

            # run dfs on left and right subtrees
            dfs(root.left, max_value)
            dfs(root.right, max_value)
            
        # begin our dfs with the root node
        # and (-10**4)-1 as max because lowest root.val is (-10**4)
        dfs(root, (-10**4)-1)

        # return the count
        return self.count
