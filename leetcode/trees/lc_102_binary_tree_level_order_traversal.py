from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # we can use a standard bfs level by level traversal
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if we are given an empty tree
        if not root:
            # simply return an empty array
            return []

        # create our standard bfs queue
        queue = deque([root])
        # init our path as an empty variable
        path = []

        # standard bfs queue while loop
        while queue:
            # init our level array
            # which will hold all node values
            # at a specific level
            level = []

            # loop through all nodes at this queue level
            for _ in range(len(queue)):
                # get the current node from the queue
                node = queue.popleft()

                # append the current node's value to the level
                level.append(node.val)

                # if the current node has a left node
                if node.left:
                    # add the left node to the queue
                    queue.append(node.left)
                # if the current node has a right node
                if node.right:
                    # add the right node to the queue
                    queue.append(node.right)

            # finally, add the entire level array to the path array
            path.append(level)

        # finally return the path array
        return path
