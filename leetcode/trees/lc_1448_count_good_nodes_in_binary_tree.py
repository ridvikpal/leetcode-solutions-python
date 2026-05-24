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
        # init our count for the number of good nodes
        self.count = 0

        # our recursive dfs function
        # which takes in a node on the path
        # and the current maximum value along the path
        def dfs(node, path_max):
            # if we are at an empty leaf node
            if not node:
                # just return immediately
                return

            # if the current node's value is greater
            # than or equal to the current maximum value
            # along the path
            # then this is the largest node along this path
            if node.val >= path_max:
                # update the current path max
                path_max = node.val
                # update the count of good nodes
                self.count += 1

            # perform dfs on the left subtree
            dfs(node.left, path_max)
            # perform dfs on the right subtree
            dfs(node.right, path_max)

        # begin our dfs with the root node
        # and a maximum value of -infinity
        dfs(root, -float('inf'))

        # finally return the count of good nodes
        return self.count
