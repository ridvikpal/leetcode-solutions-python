from collections import deque
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
    # we will use a level-by-level bfs approach
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if we're given an empty tree
        if not root:
            # simply return 0
            return 0

        # create our standard queue for bfs
        # we don't need a visited set because
        # it's a binary tree
        queue = deque([root])

        # init our depth to 0
        depth = 0

        # standard bfs loop as long as the queue is not empty
        while queue:
            # increment the depth at each level of bfs
            depth += 1

            # loop through all nodes at a specific tree level
            for _ in range(len(queue)):
                # get the current node from the queue
                current = queue.popleft()
                # if there is a left node
                if current.left:
                    # add it to the queue
                    queue.append(current.left)

                # if there is a right node
                if current.right:
                    # add it to the queue
                    queue.append(current.right)

        # finally return the depth of the tree
        return depth
